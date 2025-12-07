# app/serializers/custom_token_serializer.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # ✅ O CAMPO QUE VOCÊ PRECISA
        token['is_staff'] = bool(user.is_staff)
        token['email'] = user.email

        return token