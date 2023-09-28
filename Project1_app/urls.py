from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.CustomUserRegistrationView.as_view(), name='user-registration'),
    path('roles/',views.RolesPost.as_view(), name='RolesPost'),
    path('permissions/',views.PermissionPost.as_view(), name='PermissionsPost')
    ]