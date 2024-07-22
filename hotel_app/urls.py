
from django.urls import path
from . import views

app_name = 'hotel_app'

urlpatterns = [
    path('hotel/home', views.home,name='home'),
    path('hotel/settings', views.setting,name='setting'),
    path('hotel/hotelorders', views.h_orders,name='h_orders'),
    path('hotel/add_food', views.add_food,name='add_food'),
    path('hotel/earnings', views.earnings,name='earnings'),
    path('hotel/edit_food/<slug:f_slug>', views.edit_food,name='edit_food'),
    path('hotel/order_view/<int:or_id>', views.order_view,name='order_view'),


    
]
