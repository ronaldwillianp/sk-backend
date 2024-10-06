from rest_framework import routers
from .viewsets import UserView, UserCreateView, UserUpdateView, UserChangePasswordView
from django.urls import path, include

router = routers.SimpleRouter()

urlpatterns = [
    path(r'user/', UserView.as_view(), name='user'),
    path(r'user/create/', UserCreateView.as_view(), name='create_user'),
    path(r'user/<int:pk>/', UserUpdateView.as_view(), name='update_user'),
    path(r'user/<int:pk>/change_password', UserChangePasswordView.as_view(), name='change_password'),
    path('', include(router.urls)),
]
