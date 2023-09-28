from rest_framework import serializers
from Project1_app.models import User, Roles, Group, Permissions


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RolesSerializer(serializers.ModelSerializer):
    # Roles = serializers.CharField(max_length=100,choices=Roles.roles)
    class Meta:
        model = Roles
        fields = '__all__'


class PermissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'
