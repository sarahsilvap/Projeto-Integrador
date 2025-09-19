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
    current_status = serializers.SerializerMethodField()
    class Meta:
        model = Request
        fields = '__all__'
        many = True
        
    #Ao crirar um Request, o User é definido automaticamente por aquele que o criou
    def create(self, validated_data):
        user = self.context['request'].user
        request_instance = Request.objects.create(user_FK=user, **validated_data)

        # Cria o status inicial como 'OPEN'
        Status.objects.create(
            request_FK=request_instance,
            name='OPEN',
            changed_by_FK=user
        )

        return request_instance

    def update(self, instance, validated_data):
        user = self.context['request'].user
        new_status = self.context['request'].data.get('status')

        if new_status:
            if not user.is_staff:
                raise serializers.ValidationError("Você não tem permissão para alterar o status.")
            Status.objects.create(
                request_FK=instance,
                name=new_status,
                changed_by_FK=user
            )

        return super().update(instance, validated_data)


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        many = True