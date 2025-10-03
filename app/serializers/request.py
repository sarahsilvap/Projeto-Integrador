from rest_framework import serializers
from ..models import Request, Status
from django.utils import timezone
from .user import UserSerializer

class RequestSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField()
    user_FK = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'  # vai retornar só o name do usuário
    )
    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        request_obj = Request.objects.create(user_FK=user, **validated_data)

        # cria status inicial OPEN
        Status.objects.create(
            request_FK=request_obj,
            name='OPEN',
            changed_by_FK=user
        )

        return request_obj
        
    def get_current_status(self, obj):
        status = obj.current_status()
        return status.name if status else None

    def update(self, instance, validated_data):
        user = self.context['request'].user
        new_status = self.context['request'].data.get('status')

        # regra: não permitir edição se já estiver CLOSED
        current_status = instance.current_status()
        if current_status and current_status.name.upper() == 'CLOSED':
            raise serializers.ValidationError("Este request já está fechado e não pode ser alterado.")
        
        #Atualiza os campos normais primeiro
        instance = super().update(instance, validated_data)

        if new_status:
            if not user.is_staff:
                raise serializers.ValidationError("Você não tem permissão para alterar o status.")
            
             # regra: se tentar fechar, precisa ter passado por ONGOING e ter mensagem
            if new_status.upper() == 'CLOSED':
                if not instance.statuses.filter(name='ONGOING').exists():
                    raise serializers.ValidationError("O chamado só pode ser fechado após estar ONGOING.")
                if not instance.closing_message:
                    raise serializers.ValidationError("É obrigatório informar uma mensagem ao fechar o chamado.")
                if not instance.closing_date:
                    instance.closing_date = timezone.now()

            Status.objects.create(
                request_FK=instance,
                name=new_status,
                changed_by_FK=user
            )

        return instance