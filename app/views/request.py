from rest_framework import viewsets, serializers
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Request, RequestImage
from ..serializers import RequestSerializer, RequestImageSerializer


class RequestView(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def get_queryset(self):
            # Garantir que a exibição de 'urgency_level' seja sempre traduzida para o display
            queryset = super().get_queryset()
            # Podemos adicionar outras lógicas de filtragem ou transformação de dados aqui se necessário
            return queryset
    
    def get_queryset(self):
        user = self.request.user  # Obtendo o usuário autenticado

        # Verificando se o usuário é administrador
        if user.is_staff:
            # Administradores podem ver todas as requisições
            return Request.objects.all()

        # Usuários comuns, apenas suas requisições
        requests = Request.objects.filter(user_FK=user)

        # Se o usuário não tem nenhuma requisição, retornamos uma mensagem amigável
        if not requests.exists():
            return Response({"detail": "Nenhuma requisição encontrada para este usuário."}, status=404)

        return requests


# Serializer para RequestImage
class RequestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestImage
        fields = ['image', 'request_FK']

# Serializer para Request
class RequestSerializer(serializers.ModelSerializer):
    # Associando múltiplas imagens a uma requisição
    images = RequestImageSerializer(many=True)  # Aceitando várias imagens

    class Meta:
        model = Request
        fields = ['title', 'description', 'urgency_level', 'departament', 'user_FK', 'images']
        read_only_fields = ['user_FK']  # Evitar que o usuário altere seu próprio campo FK

    def create(self, validated_data):
        # Separando as imagens do restante dos dados
        images_data = validated_data.pop('images', [])
        # Criando a instância da requisição
        request_instance = Request.objects.create(**validated_data)

        # Criando e associando as imagens à requisição
        for image_data in images_data:
            RequestImage.objects.create(request_FK=request_instance, **image_data)

        return request_instance
