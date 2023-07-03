from django.shortcuts import render

# Create your views here.
values =[
    {'name' : 'customer','discription':'customer Can Do their Work From this Link'},
    {'name' : 'car','discription':'Car Details'},
]


def dashBoard(request):
    context ={'values' : values}
    return render(request,'DashBoard.html' ,context)
