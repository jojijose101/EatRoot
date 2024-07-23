
from django.urls import path
from . import views

app_name = 'delivery_app'

urlpatterns = [
    path('delivery/home', views.home,name='home'),
    path('delivery/settings', views.setting,name='setting'),
    path('delivery/order_view/<int:o_id>', views.order_view,name='order_view'),
    path('delivery/reached_location/<int:o_id>', views.confirm_order,name='order_confirm'),
    path('delivery/earnings', views.earnings,name='earn'),
    
]
