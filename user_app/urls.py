
from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('', views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='c_of_food'),
    path('<slug:h_slug>',views.hotels,name='h_of_food'),
    path('<slug:c_slug>/<slug:f_slug>',views.foodfind,name='foodfind'),
    path('createorder/profile/orderuser/<int:or_id>',views.order_user,name='orderuser'),


    
]