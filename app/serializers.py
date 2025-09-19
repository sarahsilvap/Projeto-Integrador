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
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.is_staff:
            data.pop('closing_date', None)
        return data
    def validate(self, attrs):
        user = self.context['request'].user
        if not user.is_staff and 'closing_date' in attrs:
            raise serializers.ValidationError("Você não tem permissão para definir a data de fechamento.")
        return attrs

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        many = True