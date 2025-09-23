
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import status

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
    filterset_fields = ['request_FK']  # Filtro por request_FK
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_status = request.data.get('name')
       
        if instance.name.upper() == 'CLOSED':
            raise ValidationError("Esse request já está fechado e não pode ser alterado.")
        
        # Verifica se está tentando fechar e já existe outro status CLOSED para o mesmo request
        if new_status == 'CLOSED':
            if Status.objects.filter(request_FK=instance.request_FK, name__iexact='CLOSED').exclude(pk=instance.pk).exists():
                raise ValidationError("Este request já foi fechado anteriormente e não pode ser fechado novamente.")
            
            if instance.name != 'IN_PROGRESS':
                return Response(
                    {'detail': 'Só é permitido fechar se o status anterior for \"IN_PROGRESS\".'},
                    status=status.HTTP_403_FORBIDDEN
                )

        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(changed_by_FK=self.request.user)

    def perform_update(self, serializer):
        serializer.save(changed_by_FK=self.request.user)

    #user_FK seja preenchido automaticamente com o usuário autenticado ao atualizar status
    def perform_update(self, serializer):
        serializer.save(changed_by_FK=self.request.user)

class RequestView(ModelViewSet):    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    
    #user_FK seja preenchido automaticamente com o usuário autenticado
    def perform_create(self, serializer):
        request_obj = serializer.save(user_FK=self.request.user)

        # Cria status inicial "OPEN"
        Status.objects.create(
            request_FK=request_obj,
            name='OPEN',
            changed_by_FK=self.request.user
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        current_status = instance.current_status()

        # Verifica se o request já está fechado
        if current_status and current_status.name.upper() == 'CLOSED':
            raise ValidationError("Este request já está fechado e não pode ser alterado.")
        
        new_status = request.data.get('status')
        message = request.data.get('closing_message')
        
        if new_status == 'CLOSED':  
            if not instance.statuses.filter(name='IN_PROGRESS').exists():
                raise ValidationError("O chamado só pode ser fechado após ter sido colocado como Em Progresso.")
            
            if not message:
                raise ValidationError("É obrigatório informar uma mensagem ao fechar o chamado.")
        
        return super().update(request, *args, **kwargs)

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


