from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

admin.site.register(User)
admin.site.register(Asset)
admin.site.register(Request)
admin.site.register(Status)
admin.site.register(Photo)

# Register your models here.
