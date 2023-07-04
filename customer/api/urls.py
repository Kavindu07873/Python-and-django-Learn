from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.getRoutes),
    path('service/' ,views.getService),
    path('service/<str:pk>/',views.getoneService),
]