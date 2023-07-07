from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from customer.models import CustomerValues
from .serializers import CustomerSerializer
from  django.shortcuts import render ,redirect
from rest_framework.views import APIView

#
@api_view(['GET'])
def getRoutes(request):
    routes =[
        'GET/api',
        'GET/api/services',
        'GET/api/createCustomer',
        'GET/api/services/:id'
    ]
    return Response (routes)

@api_view(['POST'])
def createCustomer(request):
     if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
@api_view(['PUT'])
def updateCustomer(request , pk):
    if request.method =='PUT':
        serve = CustomerValues.objects.get(id = pk)
        serializer = CustomerSerializer(serve , data=request.data)
        if serializer.is_valid():
            serializer.update(serve ,serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


