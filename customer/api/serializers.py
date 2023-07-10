# serializers.py
from rest_framework.serializers import ModelSerializer
from customer.models import CustomerValues




class CustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerValues
        fields = '__all__'

# class CarSerializer(ModelSerializer):
#     class Meta:
#         model = CarDetails
#         fields = '__all__'
#
