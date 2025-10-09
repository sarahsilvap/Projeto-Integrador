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


class Asset(models.Model):
    name = models.CharField(max_length=255)
    departament = models.CharField(max_length=100,choices=DEPARTAMENTS)
    tag_number = models.IntegerField(unique=True, blank=True)
    
    def __str__(self):
        return self.name