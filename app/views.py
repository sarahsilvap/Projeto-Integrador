from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AssetView(ModelViewSet):    
    queryset = Asset.objects.all()
    serializer_class = AssetSterializer

class StatusView(ModelViewSet):    
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class RequestView(ModelViewSet):    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class PhotoView(ModelViewSet):    
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer