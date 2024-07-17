
from django.urls import path
from . import views

app_name = 'delivery_app'

urlpatterns = [
    path('delivery/home', views.home,name='home'),
    path('delivery/settings', views.setting,name='setting'),
    
]
