import re
from django.forms import ValidationError
from django.shortcuts import redirect, render,get_object_or_404
from authenticate_users.decorators import hotel_user_required
from hotel_app.models import Hotel, Category,Food
from user_app.models import UserOrder
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@hotel_user_required
def home(request):
    h_user = request.user
    hotel = Hotel.objects.get(user=h_user)
    foods = hotel.foods.all()
    return render(request, 'h_home.html',{'foods':foods})


@hotel_user_required
def setting(request):
    try:
        hotel_profile = Hotel.objects.get(user=request.user)
        is_new_profile = False
    except Hotel.DoesNotExist:
        hotel_profile = Hotel(user=request.user)
        is_new_profile = True

    if request.method == 'POST':
        if 'image' in request.FILES:
            hotel_profile.img = request.FILES['image']
        hotel_profile.desc = request.POST.get('desc', hotel_profile.desc)
        hotel_profile.location = request.POST.get('location', hotel_profile.location)
        hotel_profile.name = request.POST.get('name', hotel_profile.name)
        contact = request.POST.get('contact', hotel_profile.contact)

        if is_new_profile: # Automatically generate a slug
            hotel_profile.slug = slugify(hotel_profile.name)  
            
        
        hotel_profile.contact = contact
        hotel_profile.save()
        return redirect('hotel_app:home')  # Redirect to the same page to avoid re-submission
    return render(request, 'h_profile.html', {'user_profile': hotel_profile, 'is_new_profile': is_new_profile})


def h_orders(request):
    STATUS = (
        ('pending','pending'),
        ('order placed','order placed'),
        ('out for delivery', 'out for delivery'),
        ('delivery compleated','delivery compleated')
    )
    hotel = Hotel.objects.get(user = request.user)
    usr_order = UserOrder.objects.filter(order__hotel=hotel)
    orders = usr_order.filter(status=STATUS[0])
    order_placed = usr_order.filter(status=STATUS[1])
    completed = usr_order.filter(status=STATUS[3])
    context = {
        'orders':orders,
        'order_placed':order_placed,
        'completed':completed

    }
   

    return render(request,'h_orders.html',context)


def add_food(request):
    if request.method == "POST":
        h_user = request.user
        name = request.POST.get('name')
        category = Category.objects.get(id = request.POST.get('category'))
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        img = request.FILES.get('image')
    
        food = Food.objects.create(name=name,category=category,price=price,img=img,desc=desc)
        food.slug = slugify(name)
        if request.POST.get('available'):
            food.available = True
    
        food.save()
        food.save()
        hotel = Hotel.objects.get(user = h_user)
        hotel.foods.add(food)
        hotel.save()
        return redirect('hotel_app:home')

    categories = Category.objects.all()
    return render(request,'h_add_food.html',{'categories':categories})

def earnings(request):
    earnings = Hotel.objects.get(user=request.user) 
    return render(request,'h_earnings.html',{'earnings':earnings})


def edit_food(request,f_slug):
    food = Food.objects.get(slug = f_slug)
    cat = Category.objects.get(name=food.category)
    Categories = Category.objects.all()

    if request.method == "POST":
        h_user = request.user
        name = request.POST.get('name')
        category = Category.objects.get(id = request.POST.get('category'))
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        img = request.FILES.get('image')
    
        
        food.slug = slugify(name)
        if request.POST.get('available'):
            food.available = True
        food.category=category
        food.price = price
        food.desc = desc
        if img:
            food.img = img
        

        
    
        food.save()
        hotel = Hotel.objects.get(user = h_user)
        hotel.foods.get(slug=f_slug)
        hotel.save()
        return redirect('hotel_app:home')


    return render(request,'h_edit_food.html',{'food':food,"cat":cat,'categories':Categories})


def order_view(request,or_id):
    STATUS = (
        ('pending','pending'),
        ('order placed','order placed'),
        ('out for delivery', 'out for delivery'),
        ('delivery compleated','delivery compleated')
    )
    order = UserOrder.objects.get(id=or_id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    if request.method == "POST":
        hotel=Hotel.objects.get(user=request.user)
        hotel.earn += earn
        hotel.save()
        order.status = STATUS[1]
        order.save()
        return redirect('hotel_app:h_orders')

    
    return render(request,'h_order_placing.html',{'foods':foods,'order':order,'earn':earn})