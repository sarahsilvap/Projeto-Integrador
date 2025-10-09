from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Request 

class StatusDashboardView(APIView):
    def get(self, request):
        # Total de requisições
        total_requests = Request.objects.count()

        # Inicializa o contador de status
        status_counts = {}

        # Para cada requisição, pega o último status
        for req in Request.objects.all():
            latest_status = req.statuses.order_by('-date_of_modification').first()
            if latest_status:
                status_name = latest_status.name
                status_counts[status_name] = status_counts.get(status_name, 0) + 1

        return Response({
            'total_requests': total_requests,
            'status_counts': status_counts
        })
