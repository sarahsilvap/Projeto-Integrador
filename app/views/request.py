from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Request
from ..serializers import RequestSerializer
from ..filters.request_filters import RequestFilter  

class RequestView(viewsets.ModelViewSet):
    """
    ViewSet para gerenciar as requisições de requests (chamados).
    """
    serializer_class = RequestSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar
    filter_backends = (DjangoFilterBackend,)  # Aplica o filtro
    filterset_class = RequestFilter    # Informa qual filtro usar

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # Aplica os filtros aqui
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
        # Este QuerySet pode ser vazio, o que é o comportamento esperado.
        requests_queryset = Request.objects.filter(user_FK=user)
        
        # 🚨 CORREÇÃO: Remova a verificação 'if not requests.exists():' que retorna Response.
        # A lista vazia será serializada corretamente.

        return requests_queryset
