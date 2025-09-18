from django.db import models

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
    ('IN_PROGRESS', 'Em andamento')
    ('CLOSED', 'Fechado'),
]

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    #Login por e-mail:
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=255)
    departament = models.CharField(max_length=100,choices=DEPARTAMENTS)
    tag_number = models.IntegerField()
    serial_number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=100, choices=STATUS)
    date_of_modification = models.DateField()
    changed_by_FK = models.ForeignKey(User, related_name='Status_changed_by_FK', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Request(models.Model):
    user_FK = models.ForeignKey(User, related_name='Request_user_FK', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField()
    asset_FK = models.ForeignKey(Asset, related_name='Request_asset_FK', on_delete=models.CASCADE)
    creation_date = models.DateField()
    closing_date = models.DateField()
    status_FK = models.ForeignKey(Status, related_name='Request_user_FK', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/')
    request_FK = models.ForeignKey(Request, related_name='Photo_request_FK', on_delete=models.CASCADE)
    



    
