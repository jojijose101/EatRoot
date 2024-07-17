from django.contrib import admin

from user_app.models import OrderItem, UserOrder

# Register your models here.

admin.site.register(OrderItem)
admin.site.register(UserOrder)

