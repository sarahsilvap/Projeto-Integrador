from django.db import models
from django.utils import timezone

class STATUS(models.TextChoices):
    OPEN = 'OPEN', 'Aberto'
    WAITING_ASSIGNEE = 'WAITING_ASSIGNEE', 'Aguardando Atribuição'
    ONGOING = 'ONGOING', 'Em Andamento'
    DONE = 'DONE', 'Concluído'
    CLOSED = 'CLOSED', 'Fechado'
    CANCELLED = 'CANCELLED', 'Cancelado'

class Status(models.Model):
    name = models.CharField(max_length=100, choices=STATUS)
    request_FK = models.ForeignKey('Request', related_name='statuses', on_delete=models.CASCADE)
    date_of_modification = models.DateTimeField(auto_now_add=True)
    changed_by_FK = models.ForeignKey('CustomUser', related_name='status_changes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        # Formatação da data para o formato brasileiro
        data_brasilia = timezone.localtime(self.date_of_modification)
        # Exibe a requisição com o status e a data da modificação
        return self.name

    def get_name(self, obj):
        return obj.get_name_display()
