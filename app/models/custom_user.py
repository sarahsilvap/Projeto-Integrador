from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..user_manager import CustomUserManager

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
