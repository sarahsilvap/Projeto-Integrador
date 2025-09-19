from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        many = True
        
class AssetSterializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
        many = True
        
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        many = True
        
class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        many = True
        
    #Ao crirar um Request, o User é definido automaticamente por aquele que o criou
    def create(self, validated_data):
        # Define status como OPEN ao criar
        validated_data['status_FK'] = Status.objects.get(name='OPEN')
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
            user = self.context['request'].user
            status_changed = 'status_FK' in validated_data and validated_data['status_FK'] != instance.status_FK

            if status_changed and not user.is_staff:
                raise serializers.ValidationError("Você não tem permissão para alterar o status.")

            updated_instance = super().update(instance, validated_data)

            # Se o status foi alterado, registra no histórico
            if status_changed:
                StatusHistory.objects.create(
                    request_FK=updated_instance,
                    status_FK=updated_instance.status_FK,
                    changed_by_FK=user
                )

            return updated_instance

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        many = True