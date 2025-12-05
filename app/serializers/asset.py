from rest_framework import serializers
from ..models import Asset

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['departament'] = instance.get_departament_display()
        return representation
