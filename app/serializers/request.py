from rest_framework import serializers
from ..models import Request, RequestImage, Status
from .request_image import RequestImageSerializer
from ..models import URGENCY_LEVELS, STATUS, DEPARTAMENTS  # Se necessário

class RequestSerializer(serializers.ModelSerializer):
    # Display do status (em português)
    current_status_display = serializers.CharField(source='current_status.get_name_display', read_only=True)

    # Novo campo para mostrar o status em inglês (valor real)
    current_status = serializers.CharField(read_only=True)  # Agora, remove-se o 'source'

    # Display de outros campos
    urgency_level_display = serializers.CharField(source='get_urgency_level_display', read_only=True)
    departament_display = serializers.CharField(source='get_departament_display', read_only=True)

    # Campos de entrada para atualizar os valores
    urgency_level_input = serializers.ChoiceField(choices=URGENCY_LEVELS.choices, required=False)
    departament_input = serializers.ChoiceField(choices=DEPARTAMENTS, required=False)
    current_status_input = serializers.ChoiceField(choices=STATUS.choices, required=False)  # Para receber o valor real do status

    user_name = serializers.CharField(source='user_FK.name', read_only=True)
    asset_name = serializers.CharField(source='asset_FK.name', read_only=True)
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

    def create(self, validated_data):
        # Atribui automaticamente o usuário autenticado
        user = self.context['request'].user
        validated_data["user_FK"] = user

        request_obj = Request.objects.create(**validated_data)

        # Se o current_status_input for fornecido, cria o status com esse valor
        current_status_input = validated_data.pop('current_status_input', None)
        if current_status_input:
            Status.objects.create(
                name=current_status_input,
                request_FK=request_obj,
                changed_by_FK=user
            )
        else:
            # Se não passar status, define como 'OPEN' por padrão
            Status.objects.create(
                name='OPEN',
                request_FK=request_obj,
                changed_by_FK=user
            )

        # Criar e associar imagens
        request_data = self.context['request']
        images = request_data.FILES.getlist('images')
        for image_file in images:
            RequestImage.objects.create(
                request_FK=request_obj,
                image=image_file
            )

        return request_obj

    def update(self, instance, validated_data):
        user = self.context['request'].user

        # Atualizando o current_status
        new_status_input = validated_data.get('current_status_input', None)
        if new_status_input:
            # Cria um novo status se o status for alterado
            Status.objects.create(
                name=new_status_input,
                request_FK=instance,
                changed_by_FK=user
            )

        # Atualiza outros campos como urgency_level e departament
        urgency_level_input = validated_data.get('urgency_level_input', None)
        if urgency_level_input:
            instance.urgency_level = urgency_level_input

        departament_input = validated_data.get('departament_input', None)
        if departament_input:
            instance.departament = departament_input

        instance = super().update(instance, validated_data)

        instance.save()  # Salva as modificações
        return instance
