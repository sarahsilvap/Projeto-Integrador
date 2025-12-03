from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import NotFound
from ..models import Request
from ..serializers import RequestSerializer

class RequestView(ModelViewSet):
    serializer_class = RequestSerializer

    def get_queryset(self):
        user = self.request.user  # Obtendo o usuário autenticado

        # Verificando se o usuário é administrador
        if user.is_staff:
            # Administradores podem ver todas as requisições
            return Request.objects.all()

        # Usuários comuns, apenas suas requisições
        requests = Request.objects.filter(user_FK=user)

        # Se o usuário não tem nenhuma requisição, retornamos um erro
        if not requests.exists():
            raise NotFound("Nenhuma requisição encontrada para este usuário.")

        return requests
