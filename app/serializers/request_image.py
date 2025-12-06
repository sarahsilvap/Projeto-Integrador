from rest_framework import serializers
from ..models import RequestImage

class RequestImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestImage
        fields = ['id', 'image', 'request_FK']
        extra_kwargs = {
            "request_FK": {"write_only": True}
        }
