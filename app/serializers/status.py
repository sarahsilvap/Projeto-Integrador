from rest_framework import serializers
from ..models import Status

class StatusSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Status
        fields = '__all__'

    def validate(self, data):
        instance = getattr(self, 'instance', None)
        new_status = data.get('name', None)

        if instance and instance.name.upper() == 'CLOSED':
            raise serializers.ValidationError("Esse request já está fechado e não pode ser alterado.")

        # Verifica se está tentando fechar e já existe outro CLOSED
        if new_status == 'CLOSED':
            request_fk = instance.request_FK if instance else data.get('request_FK')
            if Status.objects.filter(request_FK=request_fk, name__iexact='CLOSED').exclude(pk=getattr(instance, 'pk', None)).exists():
                raise serializers.ValidationError("Este request já foi fechado anteriormente e não pode ser fechado novamente.")

            if instance and instance.name != 'ONGOING':
                raise serializers.ValidationError('Só é permitido fechar se o status anterior for "ONGOING".')

        return data

    def update(self, instance, validated_data):
        validated_data['changed_by_FK'] = self.context['request'].user
        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['changed_by_FK'] = self.context['request'].user
        return super().create(validated_data)
    
    def get_name(self, obj):
        return obj.get_name_display()  # Retorna a descrição do status em português
