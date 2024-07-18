from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model


user = get_user_model()


class DelUser(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    location = models.TextField()
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='deliverygallery',default="delivery-boy_10367830.png")
    contact = models.CharField(max_length=15,blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'delivery boy'
        verbose_name_plural = 'delivery boys'
        

    def __str__(self):
        return self.name