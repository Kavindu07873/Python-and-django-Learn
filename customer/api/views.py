from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.models import Service
from .serializers import ServiceSerializer



@api_view(['GET'])
def getRoutes(request):
    routes =[
        'GET/api',
        'GET/api/services',
        'GET/api/services/:id'
    ]
    return Response (routes)

@api_view(['GET'])
def getService(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getoneService(request , pk):
    serve = Service.objects.get(id = pk)
    serializer = ServiceSerializer(serve,many=False)
    return Response(serializer.data)