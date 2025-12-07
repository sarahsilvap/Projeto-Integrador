from rest_framework import serializers
from ..models import Request, RequestImage, Status
from .request_image import RequestImageSerializer
from ..models import URGENCY_LEVELS, STATUS, DEPARTAMENTS

class RequestSerializer(serializers.ModelSerializer):
    # Campos READ-ONLY (Displays e FKs)
    current_status_display = serializers.CharField(source='current_status.get_name_display', read_only=True)
    urgency_level_display = serializers.CharField(source='get_urgency_level_display', read_only=True)
    departament_display = serializers.CharField(source='get_departament_display', read_only=True)
    creation_date = serializers.DateTimeField(format="%d/%m/%Y, às %H:%M", read_only=True)
    status = serializers.CharField(source='current_status.name', read_only=True) # Código canônico
    
    user_name = serializers.CharField(source='user_FK.name', read_only=True)
    asset_name = serializers.CharField(source='asset_FK.name', read_only=True)
    images = RequestImageSerializer(many=True, read_only=True)

    # ⚠️ NOVO: Campo temporário para receber o novo status, se for passado no payload.
    # Se você quiser que o payload use 'status_code' para criar o status:
    status_code = serializers.ChoiceField(choices=STATUS.choices, write_only=True, required=False)

    class Meta:
        model = Request
        # ✅ Liste explicitamente todos os campos do MODELO que devem ser lidos/escritos
        fields = [
            'id', 'title', 'description', 
            'urgency_level', 'departament', # Campos do modelo (usados para escrita)
            'user_FK', 'asset_FK', 
            'closing_message', 'closing_date',
            
            # ➕ Campos explícitos (read-only e temporários)
            'current_status_display', 'urgency_level_display', 'departament_display', 
            'creation_date', 'status', 'user_name', 'asset_name', 'images',
            'status_code' # Campo temporário para escrita (se você usar 'status_code' no payload)
        ]

        extra_kwargs = {
            "user_FK": {"write_only": True, "required": False},
            "asset_FK": {"write_only": True, "required": True},
            # ... o resto está OK
        }

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["user_FK"] = user

        # ⚠️ Pega o campo temporário de status do payload
        status_code = validated_data.pop('status_code', None)

        request_obj = Request.objects.create(**validated_data)

        # Cria o status
        Status.objects.create(
            name=status_code or 'OPEN', # Usa o código do payload ou 'OPEN'
            request_FK=request_obj,
            changed_by_FK=user
        )

        # ... Lógica de criação e associação de imagens
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

        # Atualizando o status (usando 'status_code' como campo de entrada)
        new_status_code = validated_data.pop('status_code', None)
        if new_status_code:
            Status.objects.create(
                name=new_status_code,
                request_FK=instance,
                changed_by_FK=user
            )

        # Atualiza campos diretamente no modelo
        if 'urgency_level' in validated_data:
            instance.urgency_level = validated_data['urgency_level']

        if 'departament' in validated_data:
            instance.departament = validated_data['departament']
            
        # O super().update já cuida de 'title', 'description', etc.
        instance = super().update(instance, validated_data)

        instance.save()
        return instance