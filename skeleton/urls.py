"""
URL configuration for skeleton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from . import views

from knox import views as knox_views
from administracion.views import LoginView

urlpatterns = [
    # Admin Panel Routing
    path('admin/', admin.site.urls),
    # Knox Routing
    path(r'api/auth/login/', LoginView.as_view(), name='knox_login'),
    path(r'api/auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path(r'api/auth/logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),


    # System Modules Routing
    path(r'api/administracion/', include('administracion.urls')),




    # Assets, APIs & Auth re-routing
    re_path(r'^(?!admin/|api/|media/|assets/|.well-known/|auth/)', views.index),
]