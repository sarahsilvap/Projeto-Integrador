from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('name',)}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )

class RequestAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista
    list_display = ('title', 'urgency_level', 'creation_date', 'departament', 'asset_FK')

    # Filtros disponíveis na barra lateral
    list_filter = ('urgency_level', 'departament', 'statuses')

    # Campos que podem ser pesquisados
    search_fields = ('title', 'description')

    def get_status(self, obj):
        return obj.statuses.order_by('-date_of_modification').first().name if obj.statuses.exists() else 'Sem status'

    get_status.admin_order_field = 'status'
    get_status.short_description = 'Status'

admin.site.register(Request, RequestAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Asset)
admin.site.register(Status)

# Register your models here.
