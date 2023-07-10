from django.shortcuts import render,redirect
from  django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import models
from .models import Service ,Topic ,Message
from .forms import ServiceForm
from django.contrib import messages


# Create your views here.


# service = [{'id':1 ,'Name':'name' },
#            {'id':2 ,'Name':'kamala'}
#            ]

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('customer')

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Admin Or Password incorrect.")
        user = authenticate(request , username = username ,password = password)

        if user is not None:
            login(request , user)
            return redirect('customer')
        else:
            messages.error(request , 'Username or Password does not exit')
    context = {'page': page}
    return  render(request,'Login.html' ,context)



def logoutUser(request):
    logout(request)
    return redirect('customer')


def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request , user)
            return redirect('customer')
        else:
            messages.error(request,'An error occured during registration')

    return render(request , 'Login.html',{'form':form})


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
    service_count = service.count()
    context = {'service': service , 'topics':topic , 'service_count':service_count}
    return render(request, 'customer.html',context)


def coading(request,pk):
    print(pk)
    serve = Service.objects.get(id=pk)
    serve_message =serve.message_set.all().order_by('-create')
    participant = serve.participants.all()
    print(participant)
    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            service = serve,
            body = request.POST.get('Msgbody')
        )
        # msg ekak dammama add venawa chat field ekata
        serve.participants.add(request.user)
        return redirect('coading' , pk = serve.id)
    context= {'service': serve ,'serve_message':serve_message
              ,'participant':participant}
    return render(request, 'Coading.html',context)

@login_required(login_url ='login')
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



@login_required(login_url ='login')
def updateService(request,pk):
   serve = Service.objects.get(id=pk)
   form = ServiceForm(instance=serve)
   print(serve.host)
   if request.user != serve.host:
       return HttpResponse('Your are not allowed here !! ')

   if request.method == 'POST':
       form = ServiceForm(request.POST , instance=serve)
       if form.is_valid():
           form.save()
           return redirect('customer')
   context = {'form':form}
   return render(request,'CustomerForm.html',context)



# @login_required(login_required ='login')
@login_required(login_url ='login')
def deleteService(request,pk):
    serve = Service.objects.get(id = pk)
    if request.user != serve.host:
        return HttpResponse('Your are not allowed here !! ')
    if request.method=='POST':
        serve.delete()
        return redirect('customer')
    return render(request,'Delete.html',{'obj': serve})