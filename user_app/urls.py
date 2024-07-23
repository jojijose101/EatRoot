
from django.urls import path
from user_app import views

app_name = 'user_app'

urlpatterns = [
    path('', views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='c_of_food'),
    path('<slug:h_slug>',views.hotels,name='h_of_food'),
    path('<slug:c_slug>/<slug:f_slug>',views.foodfind,name='foodfind'),
    path('createorder/profile/orderuser/<int:or_id>',views.order_user,name='orderuser'),
    path('order/profile/orderuser/orders_view', views.order_view,name='orders_view'),
    path('order/profile/orderuser/orders_view/<int:o_id>', views.order,name='order'),
    path('order/profile/orderuser/orders_confirm/<int:o_id>', views.order_confirm,name='order_confirm'),
    path('order/profile/customer/profile', views.setting,name='profile'),

    
]