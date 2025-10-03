from rest_framework.viewsets import ModelViewSet
from ..models import Status
from ..serializers import StatusSerializer

class StatusView(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filterset_fields = ['request_FK']
