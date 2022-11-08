from django.db import models

# Create your models here.

class Info(models.Model):
    Name=models.TextField(max_length=20)
    phone_no= models.SmallIntegerField(max_length=10)
    image= models.ImageField(upload_to= 'Information/Images', blank=True)
    Email=models.EmailField()
