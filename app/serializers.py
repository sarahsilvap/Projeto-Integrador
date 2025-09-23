from rest_framework import serializers
from .models import *
from django.utils import timezone


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
    current_status = serializers.SerializerMethodField()
    user_FK = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Request
        fields = '__all__'
        
    def get_current_status(self, obj):
        status = obj.current_status()
        return status.name if status else None

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = self.context['request'].user
        new_status = self.context['request'].data.get('status')
        
        #Atualiza os campos normais primeiro
        instance = super().update(instance, validated_data)

        if new_status:
            if not user.is_staff:
                raise serializers.ValidationError("Você não tem permissão para alterar o status.")
            
            Status.objects.create(
                request_FK=instance,
                name=new_status,
                changed_by_FK=user
            )
            #Se o novo status for 'CLOSED' e ainda não tiver data de fechamento, registra a data
            if new_status.upper() == 'CLOSED' and not instance.closing_date:
                instance.closing_date = timezone.now()
                instance.save(update_fields=['closing_date'])

        return instance

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        many = True