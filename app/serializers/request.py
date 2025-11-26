from rest_framework import serializers
from django.utils import timezone
from ..models import Request, Status


class RequestSerializer(serializers.ModelSerializer):
    # Campo calculado
    current_status = serializers.SerializerMethodField()

    # Exibir nome do usuário e do ativo (somente leitura)
    user_name = serializers.CharField(source='user_FK.name', read_only=True)
    asset_name = serializers.CharField(source='asset_FK.name', read_only=True)

    class Meta:
        model = Request
        fields = '__all__'

        extra_kwargs = {
            "user_FK": {"write_only": True, "required": False},  
            "asset_FK": {"write_only": True, "required": True},

            "creation_date": {"read_only": True},
            "closing_date": {"read_only": True},
            "closing_message": {"required": False},
        }

    # -------------------------------------------------------
    # CREATE
    # -------------------------------------------------------
    def create(self, validated_data):
        user = self.context['request'].user

        # atribui automaticamente o usuário autenticado
        validated_data["user_FK"] = user

        request_obj = Request.objects.create(**validated_data)

        # cria status inicial OPEN
        Status.objects.create(
            request_FK=request_obj,
            name='OPEN',
            changed_by_FK=user
        )

        return request_obj

    # -------------------------------------------------------
    # GET campo do status atual
    # -------------------------------------------------------
    def get_current_status(self, obj):
        status = obj.current_status()
        return status.name if status else None

    # -------------------------------------------------------
    # UPDATE
    # -------------------------------------------------------
    def update(self, instance, validated_data):
        user = self.context['request'].user
        new_status = self.context['request'].data.get('status')

        # regra: não permitir edição se já estiver CLOSED
        current_status = instance.current_status()
        if current_status and current_status.name.upper() == 'CLOSED':
            raise serializers.ValidationError(
                "Este request já está fechado e não pode ser alterado."
            )

        # Atualiza os campos normais
        instance = super().update(instance, validated_data)

        # Se houver mudança de status
        if new_status:

            # Apenas staff pode alterar status
            if not user.is_staff:
                raise serializers.ValidationError("Você não tem permissão para alterar o status.")

            # Regras específicas de fechamento
            if new_status.upper() == 'CLOSED':
                if not instance.statuses.filter(name='ONGOING').exists():
                    raise serializers.ValidationError(
                        "O chamado só pode ser fechado após estar ONGOING."
                    )

                if not instance.closing_message:
                    raise serializers.ValidationError(
                        "É obrigatório informar uma mensagem ao fechar o chamado."
                    )

                if not instance.closing_date:
                    instance.closing_date = timezone.now()

            # Cria novo status
            Status.objects.create(
                request_FK=instance,
                name=new_status,
                changed_by_FK=user
            )

        instance.save()
        return instance
