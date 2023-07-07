from django.urls import path
from . import views


urlpatterns = [
    path('' ,views.getRoutes),
    # path('service/' ,views.getService),
    path('createCustomer/Customer/' ,views.createCustomer),
    path('createCustomer/<str:pk>',views.updateCustomer),
]