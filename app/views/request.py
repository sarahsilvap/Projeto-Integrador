from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Request, RequestImage
from ..serializers import RequestSerializer

class RequestView(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as requisições de requests (chamados).
    """
    serializer_class = RequestSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def get_queryset(self):
        """
        Retorna a lista de requisições baseadas no usuário autenticado.
        Administradores podem ver todas as requisições, usuários comuns só podem ver as suas.
        """
        user = self.request.user  # Obtendo o usuário autenticado

        # Se o usuário for administrador, ele pode acessar todas as requisições
        if user.is_staff:
            return Request.objects.all()

        # Usuários comuns, apenas suas requisições
        requests = Request.objects.filter(user_FK=user)

        # Caso o usuário não tenha requisições, retorna uma mensagem amigável
        if not requests.exists():
            return Response({"detail": "Nenhuma requisição encontrada para este usuário."}, status=404)

        return requests
