from rest_framework import serializers
from django.utils import timezone
from ..models import Request, Status, RequestImage
from .request_image import RequestImageSerializer
from ..models import URGENCY_LEVELS, DEPARTAMENTS

class RequestSerializer(serializers.ModelSerializer):
    # Campo calculado
    current_status = serializers.SerializerMethodField()

    # Exibir nome do usuário e do ativo (somente leitura)
    user_name = serializers.CharField(source='user_FK.name', read_only=True)
    asset_name = serializers.CharField(source='asset_FK.name', read_only=True)

    # Exibir tradução de 'urgency_level' e 'departament' diretamente usando os métodos de exibição
    urgency_level_display = serializers.CharField(source='get_urgency_level_display', read_only=True)
    departament_display = serializers.CharField(source='get_departament_display', read_only=True)

    # Receber os valores diretamente no PATCH e POST
    urgency_level_input = serializers.ChoiceField(choices=URGENCY_LEVELS.choices, required=False)
    departament_input = serializers.ChoiceField(choices=DEPARTAMENTS, required=False)

    images = RequestImageSerializer(many=True, read_only=True)

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

        # Atribui automaticamente o usuário autenticado
        validated_data["user_FK"] = user

        # Cria a requisição
        request_obj = Request.objects.create(**validated_data)

        # Cria status inicial OPEN
        Status.objects.create(
            request_FK=request_obj,
            name='OPEN',
            changed_by_FK=user
        )

        # Processa as imagens associadas à requisição
        request_data = self.context['request']
        images = request_data.FILES.getlist('images')
        for image_file in images:
            RequestImage.objects.create(
                request_FK=request_obj,
                image=image_file
            )

        return request_obj

    # -------------------------------------------------------
    # GET campo do status atual
    # -------------------------------------------------------
    def get_current_status(self, obj):
        status = obj.current_status()
        return status.get_name_display() if status else None

    # -------------------------------------------------------
    # UPDATE
    # -------------------------------------------------------
    def update(self, instance, validated_data):
        user = self.context['request'].user
        new_status = self.context['request'].data.get('status')

        # Regra: não permitir edição se já estiver CLOSED
        current_status = instance.current_status()
        if current_status and current_status.name.upper() == 'CLOSED':
            raise serializers.ValidationError(
                "Este request já está fechado e não pode ser alterado."
            )

        # Atualiza o campo de urgency_level se passado no PATCH
        urgency_level_input = validated_data.get('urgency_level_input', None)
        if urgency_level_input:
            instance.urgency_level = urgency_level_input  # Atualiza o valor diretamente

        # Atualiza o campo de departament se passado no PATCH
        departament_input = validated_data.get('departament_input', None)
        if departament_input:
            instance.departament = departament_input  # Atualiza o valor diretamente

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

        # Processa as imagens associadas ao request
        request_data = self.context['request']
        images = request_data.FILES.getlist('images')
        for image_file in images:
            RequestImage.objects.create(
                request_FK=instance,
                image=image_file
            )

        instance.save()  # Salva as modificações no objeto
        return instance  # Retorna a instância atualizada aqui
