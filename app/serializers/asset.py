from rest_framework import serializers
from ..models import Asset

class AssetSterializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'