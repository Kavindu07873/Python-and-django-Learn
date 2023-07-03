from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Service(models.Model):
    host =models.ForeignKey(User, on_delete=models.SET_NULL , null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL , null=True)
    Service_name = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.FloatField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']



class CustomerDetails(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    nic = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    updated =models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)




class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    body = models.TextField()
    update=models.DateTimeField(auto_now=True)
    create =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]




