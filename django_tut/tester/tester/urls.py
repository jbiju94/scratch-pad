"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from adoptions import views as adoption
from api import views as api

from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # Path to admin of one application
    path('admin/', admin.site.urls),
    # Sample URL path 
    path('', adoption.home, name='home'),
    
    # Sample URL Path with value passed
    path('adoptions/<int:id>/' , adoption.view_detail, name="detail"), # regrex not used from django 2
    
    # URL Paths included from url file in Class Based Application
    path('class/',include('tester_class.urls')),

    # rest_framework
    path('api-auth/', include('rest_framework.urls')),

    # api
    path('api/', api.IdealWeight, name='weight')
]
