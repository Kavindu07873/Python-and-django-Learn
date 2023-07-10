from django.urls import path
from . import views
from .views import YourModelViewSet

urlpatterns = [
    path('' ,views.getRoutes),
    path('createCustomer/' ,views.getCustomerVallues),
    path('createCustomer/Customer/' ,views.createCustomer),
    # path('createCar/Car/' ,views.createCar),
    path('createCustomer/<str:pk>',views.updateCustomer),
    # path('createCustomer/<str:pk>',views.deleteCustomer),
    path('createCustomer/<int:id>/', YourModelViewSet.as_view({'delete': 'destroy'}), name='yourmodel-delete'),
]