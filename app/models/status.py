from django.db import models
from django.utils import timezone

class STATUS(models.TextChoices):
    OPEN = 'OPEN'
    WAITING_ASSIGNEE = 'WAITING_ASSIGNEE'
    ONGOING = 'ONGOING'
    DONE = 'DONE'
    CLOSED = 'CLOSED'
    CANCELLED = 'CANCELLED'


class Status(models.Model):
    name = models.CharField(max_length=100, choices=STATUS)
    request_FK = models.ForeignKey('Request', related_name='statuses', on_delete=models.CASCADE)
    date_of_modification = models.DateTimeField(auto_now_add=True)
    changed_by_FK = models.ForeignKey('CustomUser', related_name='status_changes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        data_brasilia = timezone.localtime(self.date_of_modification)
        return f"{self.request_FK.title} → {self.name} em {data_brasilia.strftime('%d/%m/%Y às %H:%M:%S')}"
