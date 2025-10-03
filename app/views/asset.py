from rest_framework.viewsets import ModelViewSet
from ..models import Asset
from ..serializers import AssetSterializer

class AssetView(ModelViewSet):    
    queryset = Asset.objects.all()
    serializer_class = AssetSterializer