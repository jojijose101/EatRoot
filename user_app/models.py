import uuid
from django.contrib.auth import get_user_model
from hotel_app.models import Food, Hotel
from django.db import models
from django.urls import reverse

user = get_user_model()

class OrderFood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def q_total(self):
        return self.food.price * self.quantity
    
class OrderItem(models.Model):
    o_id = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    o_food= models.ManyToManyField(OrderFood)  
    del_charge = models.IntegerField(default=20)
    total_amount = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'
    def __str__(self):
        return f'{self.user}'
    

class UserOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('order_placed', 'Order Placed'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivery_completed', 'Delivery Completed')  # Corrected spelling
    )
    PAYMENT_CHOICES = (
        ('online_pay', 'Online Payment'),
        ('COD', 'Cash on Delivery')
    )
    
    customer = models.CharField(max_length=250)
    order = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.BigIntegerField()
    country = models.CharField(max_length=250)
    zip = models.IntegerField()
    notes = models.TextField()
    status = models.CharField(max_length=250,choices=STATUS_CHOICES,default=STATUS_CHOICES[0])
    payment_type = models.CharField(max_length=250,choices=PAYMENT_CHOICES)
    payment = models.BooleanField(default=False)
    delivery_b = models.IntegerField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    otp = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.customer
    def get_url(self):
        return reverse('user_app:orderuser',args=[self.id])  
    
    def __str__(self):
        return f'{self.customer}'
    

class Customer(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    location = models.TextField()
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='cutomergallery',default="user-profile.jpg")
    contact = models.CharField(max_length=15,blank=True, null=True)
    
    def __str__(self):
        return self.name


