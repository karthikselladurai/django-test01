from rest_framework import serializers
from .models import UserModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name', 'mobileNumber', 'email', 'password', 'created_at', 'updated_at']
