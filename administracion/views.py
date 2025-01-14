from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

# Knox Configuration
class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)