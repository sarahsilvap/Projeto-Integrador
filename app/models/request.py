from django.db import models

class URGENCY_LEVELS(models.TextChoices):
    LOW = 'LOW', 'Baixa' #permite múltiplas opções
    MEDIUM = 'MEDIUM', 'Médio'
    HIGH = 'HIGH', 'Alta'
    EXTRA_HIGH = 'EXTRA_HIGH', 'Extremamente alta'

DEPARTAMENTS = [
    ('LIBRARY', 'Biblioteca'),
    ('ADMINISTRATIVE_BUILDING', 'Secretaria'),
    ('TEACHERS_ROOM', 'Sala dos Professores'),
    ('CLASSROOM', 'Sala de Aula'),
    ('LABORATORY', 'Laboratório'),
    ('COMPUTER_LAB', 'Laboratório de Informática'),
    ('CAFETERIA', 'Refeitório'),
    ('AUDITORIUM', 'Auditório'),
    ('MUSIC_ROOM', 'Sala de Música'),
    ('ART_ROOM', 'Sala de Artes'),
    ('STORAGE_ROOM', 'Depósito'),
    ('PRINCIPAL_OFFICE', 'Diretoria'),
    ('NURSE_OFFICE', 'Enfermaria'),
    ('RECEPTION', 'Recepção'),
    ('STAFF_ROOM', 'Sala de Funcionários'),
]

class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    urgency_level = models.CharField(max_length=50,
                                     choices=URGENCY_LEVELS.choices,
                                     default=URGENCY_LEVELS.LOW)
    departament = models.CharField(max_length=100,choices=DEPARTAMENTS)
    asset_FK = models.ForeignKey('Asset', related_name='Request_asset_FK', on_delete=models.CASCADE)
    user_FK = models.ForeignKey('CustomUser', related_name='Request_user_FK', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    closing_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    # Status atual do chamado
    def current_status(self):
        return self.statuses.order_by('-date_of_modification').first()

class RequestImage(models.Model):
    image = models.FileField(upload_to='request_images')
    request_FK = models.ForeignKey('Request',
                                related_name='images',
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.task_FK.id}-{self.id}'