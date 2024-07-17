
from django.urls import path
from . import views

app_name = 'hotel_app'

urlpatterns = [
    path('hotel/home', views.home,name='home'),
    path('hotel/settings', views.setting,name='setting'),
    
]
