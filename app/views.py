
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *

class UserView(ModelViewSet):    
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AssetView(ModelViewSet):    
    queryset = Asset.objects.all()
    serializer_class = AssetSterializer

class StatusView(ModelViewSet):    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    
    #user_FK seja preenchido automaticamente com o usuário autenticado ao criar
    def perform_create(self, serializer):
        serializer.save(changed_by_FK=self.request.user)

    #user_FK seja preenchido automaticamente com o usuário autenticado ao atualizar status
    def perform_update(self, serializer):
        serializer.save(changed_by_FK=self.request.user)

class RequestView(ModelViewSet):    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    #user_FK seja preenchido automaticamente com o usuário autenticado
    def perform_create(self, serializer):
        serializer.save(user_FK=self.request.user)


@api_view(['POST'])
def upload_image(request):
    image_file = request.FILES.get('photo')
    id_request = request.POST.get('request_id')

    if not image_file or not id_request:
        return Response({"erro": "Dados incompletos"}, status=400)

    request_obj = get_object_or_404(Request, id=id_request)
    nova_foto = Photo(photo=image_file, request_FK=request_obj)
    nova_foto.save()
    return Response({"mensagem": "Imagem enviada com sucesso"})


