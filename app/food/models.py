from django.db import models
# Create your models here.


class Pension(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to= 'post', blank =True)
    price = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    check_in = models.CharField(max_length=100)
    check_out = models.CharField(max_length=100)
    room = models = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    theme = models.CharField(max_length=100)