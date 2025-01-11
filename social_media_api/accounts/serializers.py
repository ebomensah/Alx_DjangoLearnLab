from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import serializers, status 
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(*validated_data)
        Token.objects.create(user=user)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        # Authenticate user based on username and password
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        # If authentication is successful, return the user and token
        token, created = Token.objects.get_or_create(user=user)
        return {
            'user': user,
            'token': token.key
        }