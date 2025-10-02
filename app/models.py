from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import CustomUserManager
from django.utils import timezone


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

STATUS = [
    ('OPEN', 'Em Aberto'),
    ('IN_PROGRESS', 'Em andamento'),
    ('CLOSED', 'Fechado'),
]

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['name']
    
    #Login por e-mail:
    USERNAME_FIELD = "email"
    
    objects = CustomUserManager()

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=255)
    departament = models.CharField(max_length=100,choices=DEPARTAMENTS)
    tag_number = models.IntegerField(unique=True, blank=True)
    serial_number = models.CharField(unique=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Request(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    departament = models.CharField(max_length=100,choices=DEPARTAMENTS)
    asset_FK = models.ForeignKey(Asset, related_name='Request_asset_FK', on_delete=models.CASCADE)
    user_FK = models.ForeignKey(CustomUser, related_name='Request_user_FK', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now=True)
    closing_date = models.DateTimeField(null=True, blank=True)
    closing_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    # Status atual do chamado
    def current_status(self):
        return self.statuses.order_by('-date_of_modification').first()

class Status(models.Model):
    name = models.CharField(max_length=100, choices=STATUS)
    request_FK = models.ForeignKey(Request, related_name='statuses', on_delete=models.CASCADE)
    date_of_modification = models.DateTimeField(auto_now_add=True)
    changed_by_FK = models.ForeignKey(CustomUser, related_name='status_changes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        data_brasilia = timezone.localtime(self.date_of_modification)
        return f"{self.request_FK.title} → {self.name} em {data_brasilia.strftime('%d/%m/%Y às %H:%M:%S')}"

class Photo(models.Model):
    photo = models.ImageField(upload_to='fotos/')
    request_FK = models.ForeignKey(Request, related_name='Photo_request_FK', on_delete=models.CASCADE)
    



    
