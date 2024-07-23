from django.shortcuts import redirect, render,get_object_or_404
from hotel_app.models import Hotel, Category,Food
from authenticate_users.models import User
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib.auth.hashers import make_password
# Create your views here.


# for user authentication 

def extract_signup(name,email,pasw1,request):
    user = User.objects.create_user(role="CUSTOMER",username = name, email=email, password=pasw1)
    if user is None:
        return redirect('auth_app:signin')
    user.save()
    user_login = auth.authenticate(username=name, password=pasw1, role="CUSTOMER")
    auth.login(request, user_login)
    return redirect('user_app:profile')
    

def signup(request):
    if request.method != 'POST':
        return render(request,'signup.html')
    name = request.POST['username']
    email = request.POST['email']
    pasw1 = request.POST['password1']
    pasw2 = request.POST['password2']
    if len(pasw1) >8:
        messages.info(request,"sorry, Password must be 8 character")
        return redirect('auth_app:signup')
    elif pasw1 == pasw2:
        if User.objects.filter(username=name):
            messages.info(request,"sorry, username already exist")
            return redirect('auth_app:signup')
        elif User.objects.filter(email=email):
            messages.info(request,"sorry, Email already exist")
            return redirect('auth_app:signup')
        else:
            return extract_signup(name,email,pasw1,request)

    else:
        messages.info(request,"sorry, password doesn't match")
        return redirect('auth_app:signup')


def signin(request):
    if request.method != 'POST':
        return render(request, 'signin.html')
    name = request.POST['username']
    pasw = request.POST['password']
    role = 'CUSTOMER'
    user = auth.authenticate(username=name, password=pasw,role=role)
    print(name,pasw,user)
    if user is not None:
        login(request, user)
        return redirect('user_app:home')
    else:
        messages.error(request, 'Invalid login credentials')
        return redirect('auth_app:signin')
    
def signout(request):
    logout(request)
    return redirect('user_app:home')
 


# for hotel authentication 

def h_extract_signup(name,email,pasw1,request):

    user = User.objects.create_user(role="HOTEL",username = name, email=email, password=pasw1)
    if user is None:
        return redirect('auth_app:h_signin')
    user.save()
    user_login = auth.authenticate(username=name, password=pasw1, role="HOTEL")
    auth.login(request, user_login)
    return redirect('hotel_app:setting')
    

def h_signup(request):
    if request.method != 'POST':
        return render(request,'h_signup.html')
    name = request.POST['username']
    email = request.POST['email']
    pasw1 = request.POST['password1']
    pasw2 = request.POST['password2']
    if len(pasw1) >8:
        messages.info(request,"sorry, Password must be 8 character")
        return redirect('auth_app:h_signup')
    elif pasw1 == pasw2:
        if User.objects.filter(username=name):
            messages.info(request,"sorry, username already exist")
            return redirect('auth_app:h_signup')
        elif User.objects.filter(email=email):
            messages.info(request,"sorry, Email already exist")
            return redirect('auth_app:h_signup')
        else:
            return h_extract_signup(name,email,pasw1,request)

    else:
        messages.info(request,"sorry, password doesn't match")
        return redirect('auth_app:h_signup')


def h_signin(request):
    if request.method != 'POST':
        return render(request, 'h_signin.html')
    name = request.POST['username']
    pasw = request.POST['password']
    role = 'HOTEL'
    user = auth.authenticate(username=name, password=pasw,role=role)
    print(name,pasw,user)
    if user is not None:
        login(request, user)
        return redirect('hotel_app:home')
    else:
        messages.error(request, 'Invalid login credentials')
        return redirect('auth_app:h_signin')
    
def h_signout(request):
    logout(request)
    return redirect('hotel_app:home')
 


# for user authentication 

def d_extract_signup(name,email,pasw1,request):

    user = User.objects.create_user(role="DELIVERY",username = name, email=email, password=pasw1)
    if user is None:
        return redirect('auth_app:d_signin')
    user.save()
    user_login = auth.authenticate(username=name, password=pasw1)
    auth.login(request, user_login)
    return redirect('delivery_app:setting')
    

def d_signup(request):
    if request.method != 'POST':
        return render(request,'d_signup.html')
    name = request.POST['username']
    email = request.POST['email']
    pasw1 = request.POST['password1']
    pasw2 = request.POST['password2']
    if len(pasw1) >8:
        messages.info(request,"sorry, Password must be 8 character")
        return redirect('auth_app:d_signup')
    elif pasw1 == pasw2:
        if User.objects.filter(username=name):
            messages.info(request,"sorry, username already exist")
            return redirect('auth_app:d_signup')
        elif User.objects.filter(email=email):
            messages.info(request,"sorry, Email already exist")
            return redirect('auth_app:d_signup')
        else:
            return d_extract_signup(name,email,pasw1,request)

    else:
        messages.info(request,"sorry, password doesn't match")
        return redirect('auth_app:d_signup')


def d_signin(request):
    if request.method != 'POST':
        return render(request, 'd_signin.html')
    name = request.POST['username']
    pasw = request.POST['password']
    role = 'DELIVERY'
    user = auth.authenticate(username=name, password=pasw,role=role)
   
    if user is not None:
        login(request, user)
        return redirect('delivery_app:home')
    else:
        messages.error(request, 'Invalid login credentials')
        return redirect('auth_app:d_signin')
    
def d_signout(request):
    logout(request)
    return redirect('delivery_app:home')

def choose(request):
    return render(request,'choose.html')
 