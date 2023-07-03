"""
URL configuration for Learn5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# """
from django.contrib import admin
from django.urls import path,include
from  . import  views
urlpatterns = [
    path('customer/',views.customer, name='customer'),
    path('customer/<str:pk>/',views.coading, name='coading'),
    path('create_Service/',views.createService, name='create_Service'),
    path('update_service/<str:pk>/',views.updateService, name='update_service'),
    path('delete_service/<str:pk>/',views.deleteService, name='delete_service'),

]
