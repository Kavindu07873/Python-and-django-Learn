from django.shortcuts import render,redirect
from  django.db.models import Q
from django.http import  HttpResponse
from . import models
from . import models
# Create your views here.
from .models import Service ,Topic
from .forms import ServiceForm

# service = [{'id':1 ,'Name':'name' },
#            {'id':2 ,'Name':'kamala'}
#            ]


def customer(request):
    q = request.GET.get('q')if request.GET.get('q') != None else ''
    # service = Service.objects.filter(topic__name__icontains=q)
    service = Service.objects.filter(
        Q(topic__name__icontains=q) |
        Q(Service_name__icontains =q) |
        Q(qty__icontains =q)|
        Q(price__icontains =q)
    )
    topic = Topic.objects.all()
    context = {'service': service , 'topics':topic}
    return render(request, 'customer.html',context)


def coading(request,pk):
    print(pk)
    serve = Service.objects.get(id=pk)
    context= {'service': serve}
    return render(request, 'Coading.html',context)


def createService(request):
    form = ServiceForm()
    if request.method =='POST':
        print(request.POST)
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    context ={'form':form}
    return render(request, 'CustomerForm.html' , context)


def updateService(request,pk):
   serve = Service.objects.get(id=pk)
   form = ServiceForm(instance=serve)
   if request.method == 'POST':
       form = ServiceForm(request.POST , instance=serve)
       if form.is_valid():
           form.save()
           return redirect('customer')
   context = {'form':form}
   return render(request,'CustomerForm.html',context)



def deleteService(request,pk):
    serve = Service.objects.get(id = pk)
    if request.method=='POST':
        serve.delete()
        return redirect('customer')
    return render(request,'Delete.html',{'obj': serve})