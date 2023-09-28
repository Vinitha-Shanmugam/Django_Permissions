from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework import generics
from . import models
from . import serializers
from Project1_app.models import User, Group, Roles, Permissions, RolesPermissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import random
import string
from Project1_app.models import Permissions




class CustomUserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            hashed_password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = hashed_password
            user = serializer.save()
            response_data = {
                'message': 'Registered successfully',
                'error_details': None,
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PermissionPost(generics.CreateAPIView):
    serializer_class = serializers.PermissionCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.PermissionCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                'message': 'Registered successfully',
                'error_details': None,
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RolesPost(generics.CreateAPIView):
    serializer_class = serializers.RolesSerializer

    def post(self, request, *args, **kwargs):
        serializer = serializers.RolesSerializer(data=request.data)
        if serializer.is_valid():

            user = serializer.save()
            role = serializer.validated_data.get('roles')
            if role == 'admin':
                admin_group, created = Group.objects.get_or_create(name='admin')
                permissions = Permissions.objects.filter(
                    codename__in=['Create_Details', 'View_Details', 'Update_Details', 'Delete_Details']
                )

                # Create separate RolesPermissions objects for each permission
                for permission in permissions:
                    roles_permission = RolesPermissions(group_id=admin_group.id, permission_id=permission.id)
                    roles_permission.save()

            elif role == 'user1':
                user1_group, created = Group.objects.get_or_create(name='user1')
                permissions = Permissions.objects.filter(
                    codename__in=['Create_Details', 'View_Details']
                )

                # Create separate RolesPermissions objects for each permission
                for permission in permissions:
                    roles_permission = RolesPermissions(group_id=user1_group.id, permission_id=permission.id)
                    roles_permission.save()

            elif role == 'user2':
                user2_group, created = Group.objects.get_or_create(name='user2')
                permissions = Permissions.objects.filter(
                    codename__in=['Create_Details', 'View_Details', 'Update_Details']
                )

                # Create separate RolesPermissions objects for each permission
                for permission in permissions:
                    roles_permission = RolesPermissions(group_id=user2_group.id, permission_id=permission.id)
                    roles_permission.save()

            response_data = {
                'message': 'Registered successfully',
                'error_details': None,
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
