from django.db import models
# Create your models here.


class Pension(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to= 'post', blank =True)
    price = models.CharField(max_length=100)
    address = models.TextField(max_length=100, blank=True)
    check_in = models.CharField(max_length=100,blank=True)
    check_out = models.CharField(max_length=100,blank=True)
    room = models.CharField(max_length=100,blank=True)
    info = models.TextField(max_length=100,blank=True)
    theme = models.CharField(max_length=100,blank=True)
    pldx = models.IntegerField()