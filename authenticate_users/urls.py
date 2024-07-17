

from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path("home/signup/signup",views.signup,name='signup'),
    path("home/signin/signin",views.signin,name='signin'),
    path("home/signout/signout",views.signout,name='signout'),
    path("home/signup/hotel-signup",views.h_signup,name='h_signup'),
    path("home/signin/hotel-signin",views.h_signin,name='h_signin'),
    path("home/signout/hotel-signout",views.h_signout,name='h_signout'),
    path("home/signup/delivery-signup",views.d_signup,name='d_signup'),
    path("home/signin/delivery-signin",views.d_signin,name='d_signin'),
    path("home/signout/delivery-signout",views.d_signout,name='d_signout'),
    
    path("home/choose/choose",views.choose,name='choose'),
    
    
]










