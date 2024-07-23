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

@hotel_user_required
def h_orders(request):
    try:
        hotel = Hotel.objects.get(user=request.user)
    except Hotel.DoesNotExist:
        # Handle the case where the hotel for the current user does not exist
        hotel = None
    
    if hotel:
        user_orders = UserOrder.objects.filter(order__hotel=hotel)
        orders_pending = user_orders.filter(status='pending')
        orders_placed = user_orders.filter(status='order_placed')
        orders_out_for_delivery = user_orders.filter(status='out_for_delivery')
        orders_completed = user_orders.filter(status='delivery_completed')
        
        context = {
            'orders_pending': orders_pending,
            'orders_placed': orders_placed,
            'orders_out_for_delivery': orders_out_for_delivery,
            'orders_completed': orders_completed,
        }
    else:
        # Handle the case where the hotel is not found or does not exist
        context = {}
    
    return render(request, 'h_orders.html', context)
@hotel_user_required
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

@hotel_user_required
def earnings(request):
    earnings = Hotel.objects.get(user=request.user) 
    return render(request,'h_earnings.html',{'earnings':earnings})

@hotel_user_required
def edit_food(request,f_slug):
    food = Food.objects.get(slug = f_slug)
    cat = Category.objects.get(name=food.category)
    Categories = Category.objects.all()
   

    if request.method == "POST":
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
        hotel = Hotel.objects.get(user = request.user)
        hotel.foods.get(slug=f_slug)
        hotel.save()
        return redirect('hotel_app:home')


    return render(request,'h_edit_food.html',{'food':food,"cat":cat,'categories':Categories})

@hotel_user_required
def order_view(request,or_id):
   
    order = UserOrder.objects.get(id=or_id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    hotel=Hotel.objects.get(user=request.user)
    if request.method == "POST":
        hotel.earn += earn
        hotel.save()
        order.status = 'order_placed'
        order.save()
        return redirect('hotel_app:h_orders')

    
    return render(request,'h_order_placing.html',{'foods':foods,'order':order,'earn':earn})