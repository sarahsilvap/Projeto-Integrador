from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Request 
from django.db.models import Count

class TicketsByDepartamentView(APIView):
    def get (self, request):
        total_requests = Request.objects.count()

        departament_counts_qs = (
            Request.objects
            .values('departament')
            .annotate(count=Count('id'))
        )

        departament_counts = {
            entry['departament']: entry['count']
            for entry in departament_counts_qs
        }

        return Response({
            'total_requests': total_requests,
            'by_departament': departament_counts
        })
