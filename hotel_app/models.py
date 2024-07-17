from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model


user = get_user_model()


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='category')
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def get_url(self):
        return reverse('user_app:c_of_food',args=[self.slug])

    def __str__(self):
        return self.name
    


class Food(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='foods_gallery')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('user_app:foodfind',args=[self.category.slug,self.slug])


    class Meta:
        ordering = ('name',)
        verbose_name = 'food'
        verbose_name_plural = 'foods'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    foods = models.ManyToManyField(Food)
    location = models.TextField()
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='hotelgallery',default="hoteldefault.jpg")
    contact = models.IntegerField()
    class Meta:
        ordering = ('name',)
        verbose_name = 'hotel'
        verbose_name_plural = 'hotels'
        
    def get_url(self):
        return reverse('user_app:h_of_food',args=[self.slug])

    def __str__(self):
        return self.name
   