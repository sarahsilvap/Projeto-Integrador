from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import DEPARTAMENTS 

class DepartmentChoicesView(APIView):
    # Protege o endpoint (apenas usuários logados podem ver as opções)
    permission_classes = [IsAuthenticated] 

    def get(self, request, format=None):
        choices_list = []
        
        # Converte a lista de tuplas [(value, display_name)] para JSON [{'value': '...', 'name': '...'}]
        for value, display_name in DEPARTAMENTS:
            choices_list.append({
                'value': value,           
                'name': str(display_name) 
            })
        
        # Retorna a lista formatada
        return Response(choices_list)