from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import Request, RequestImage, Status, Asset
from .request_image import RequestImageSerializer
from ..models import URGENCY_LEVELS, STATUS, DEPARTAMENTS # Assumindo que STATUS é um Enum ou Choices

class RequestSerializer(serializers.ModelSerializer):
    # Campos READ-ONLY (Displays e FKs)
    current_status_display = serializers.CharField(source='current_status.get_name_display', read_only=True)
    urgency_level_display = serializers.CharField(source='get_urgency_level_display', read_only=True)
    departament_display = serializers.CharField(source='get_departament_display', read_only=True)
    creation_date = serializers.DateTimeField(format="%d/%m/%Y, às %H:%M", read_only=True)
    status = serializers.CharField(source='current_status.name', read_only=True) # Código canônico
    
    user_name = serializers.CharField(source='user_FK.name', read_only=True)
    
    # ⚠️ Alterado: Usamos 'tag_asset' para input, mas o SlugRelatedField ainda mapeia para 'asset_FK'
    # O SlugRelatedField já faz a busca do Asset por tag_number e atribui à asset_FK
    tag_asset = serializers.SlugRelatedField(
        queryset=Asset.objects.all(),
        slug_field='tag_number', # O campo que será usado para lookup e escrita
        source='asset_FK',       # Indica que o valor deve ser salvo no campo 'asset_FK' do Request
        write_only=True,         # Garante que ele só aparece na entrada (POST/PUT)
        # O campo é requerido apenas na criação, mas o 'required=False' será tratado no 'extra_kwargs'
    )
    
    # Campos READ-ONLY para o asset
    asset_tag_number_read = serializers.CharField(source='asset_FK.tag_number', read_only=True)
    asset_name = serializers.CharField(source='asset_FK.name', read_only=True)
    images = RequestImageSerializer(many=True, read_only=True)

    # Campo temporário para receber o novo status, se for passado no payload.
    status_code = serializers.ChoiceField(choices=STATUS.choices, write_only=True, required=False)

    class Meta:
        model = Request
        fields = [
            'id', 'title', 'description', 
            'urgency_level', 'departament', # Campos do modelo (usados para escrita)
            'user_FK', 'asset_FK', # Incluí 'asset_FK' para garantir que ele esteja no validated_data
            'closing_message', 'closing_date',
            
            # ➕ Campos explícitos (read-only e temporários)
            'current_status_display', 'urgency_level_display', 'departament_display', 
            'creation_date', 'status', 'user_name', 'asset_name', 'images', 
            
            # O campo de entrada para o Asset. 
            'tag_asset', # Este é o campo de entrada (write_only)
            
            # Campos de leitura do Asset
            'asset_tag_number_read', 'status_code' 
        ]

        # 🚨 CORREÇÃO ESSENCIAL
        extra_kwargs = {
            "user_FK": {"write_only": True, "required": False},
            
            # 1. Tornar 'asset_FK' não obrigatório no Serializer, pois ele será preenchido
            # indiretamente pelo 'tag_asset' e na criação.
            "asset_FK": {"write_only": True, "required": False},
            
            # 2. Tornar 'departament' não obrigatório, pois será preenchido
            # automaticamente com base no Asset.
            "departament": {"required": False, "allow_null": True}, 
            
            # Renomeei 'asset_tag_number' para 'tag_asset' (campo de entrada)
            # e 'asset_tag_number_read' para 'asset_tag_number_read' (campo de leitura)
        }
    
    # Adicionamos um validador para garantir que 'tag_asset' (que mapeia para asset_FK)
    # é passado na CRIAÇÃO (POST)
    def validate(self, data):
        # Na criação, 'tag_asset' é obrigatório.
        if self.instance is None and not data.get('asset_FK'):
             # O SlugRelatedField já validou se o número da tag existe e populou 'asset_FK'
             # Se 'asset_FK' não está presente, significa que o campo de entrada 'tag_asset' não foi enviado.
             # Se o usuário não enviou o 'tag_asset' (entrada), levante o erro.
             raise serializers.ValidationError({"tag_asset": "This field is required on creation."})

        # 🚨 LÓGICA CHAVE: Puxa o departamento do Asset encontrado pelo tag_asset
        asset_instance = data.get('asset_FK')
        if asset_instance:
            data['departament'] = asset_instance.departament
            
        return data

    def to_representation(self, instance):
        """Mapeia os campos para o JSON de saída."""
        data = super().to_representation(instance)
        
        # Mapeia o campo de leitura para o nome que queremos no JSON de saída
        # Renomeia o campo 'asset_tag_number_read' de volta para 'tag_asset' (ou 'asset_tag_number')
        if 'asset_tag_number_read' in data:
            # Você pode escolher o nome final, aqui uso 'asset_tag_number'
            data['asset_tag_number'] = data.pop('asset_tag_number_read')
        
        # Remove o campo de entrada 'tag_asset' se ele aparecer
        data.pop('tag_asset', None)
        
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data["user_FK"] = user

        # ⚠️ Pega o campo temporário de status do payload
        status_code = validated_data.pop('status_code', None)

        # O 'departament' e 'asset_FK' já foram preenchidos no método validate().
        request_obj = Request.objects.create(**validated_data)

        # Cria o status
        Status.objects.create(
            name=status_code or 'OPEN', # Usa o código do payload ou 'OPEN'
            request_FK=request_obj,
            changed_by_FK=user
        )

        # ... Lógica de criação e associação de imagens
        # Note: Esta lógica de imagens só funciona para MultiPartParser/FormParser.
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
                changed_by_by_FK=user
            )

        # O 'departament' já foi preenchido no método validate() se 'tag_asset' foi atualizado.
        # O super().update já cuida de 'title', 'description', etc., incluindo 'departament' se estiver no validated_data.
        instance = super().update(instance, validated_data)

        instance.save()
        return instance