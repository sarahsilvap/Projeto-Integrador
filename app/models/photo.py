from django.db import models

class Photo(models.Model):
    photo = models.ImageField(upload_to='fotos/')
    request_FK = models.ForeignKey('Request', related_name='Photo_request_FK', on_delete=models.CASCADE)
    



    
