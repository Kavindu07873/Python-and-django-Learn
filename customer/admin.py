from django.contrib import admin
from  . import models
# Register your models here.

from .models import Service
from .models import CustomerDetails ,Topic ,Message ,CustomerValues


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('host','topic','Service_name','qty','price')


class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display = ('name','address','nic','image_url','updated','created')



class CustomerValuesAdmin(admin.ModelAdmin):
    list_display = ('name','address','email','conNo','nic','password','updated','created')



admin.site.register(Service,ServiceAdmin)

admin.site.register(Topic)
# admin.site.register(CarDetails)


admin.site.register(CustomerValues,CustomerValuesAdmin)

admin.site.register(Message)

admin.site.register(CustomerDetails,CustomerDetailsAdmin)