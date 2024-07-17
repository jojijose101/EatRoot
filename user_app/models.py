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
    id = models.IntegerField(primary_key=True)
    o_id = models.UUIDField(default=uuid.uuid4)
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    o_food= models.ManyToManyField(OrderFood)  
    del_charge = models.IntegerField(default=20)
    total_amount = models.IntegerField()
    active = models.BooleanField(default=True)
    class Meta:
        db_table = 'CartItem'

    def get_url(self):
        return reverse('user_app:orderuser',args=[self.id])  
    
    def __str__(self):
        return f'{self.user}'
    

class UserOrder(models.Model):
    STATUS = (
        ('pending','pending'),
        ('order placed','order placed'),
        ('hotel done','hotel done'),
        ('out for delivery', 'out for delivery'),
        ('delivery compleated','delivery compleated')
    )
    PAYMENT = (
        ('online pay', 'online pay'),
        ('COD','COD')
    )
    customer = models.CharField(max_length=250)
    order = models.ForeignKey(OrderFood,on_delete=models.CASCADE)
    address = models.TextField()
    mobile = models.IntegerField()
    country = models.CharField(max_length=250)
    zip = models.IntegerField()
    notes = models.TextField()
    status = models.CharField(max_length=250,choices=STATUS,default=STATUS[0])
    payment_type = models.CharField(max_length=250,choices=PAYMENT)
    payment = models.BooleanField(default=False)
    delivery_b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.customer
