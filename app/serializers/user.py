from rest_framework import serializers
from ..models import CustomUser
from rest_framework.relations import SlugRelatedField

class UserSerializer(serializers.ModelSerializer):
    groups = SlugRelatedField(
        many = True,
        read_only = True,
        slug_field = 'name',
    )
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'is_staff', 'is_active', 'groups']
