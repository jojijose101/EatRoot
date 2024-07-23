from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from authenticate_users.decorators import customer_required
from delivery_app.models import DelUser
from hotel_app.models import Hotel, Category,Food
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
import random
from django.template.defaultfilters import slugify
from django.contrib.auth import authenticate, login, logout, get_user
from authenticate_users.decorators import customer_required, hotel_user_required
from.models import Customer, OrderFood, OrderItem, UserOrder

# Create your views here.

def home(request,c_slug =None):
    c_page = None
    foods = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        foods = Food.objects.all().filter(category=c_page)
    else:
        foods = Food.objects.all()
    paginator = Paginator(foods,8)
    try:
        page = int(request.GET.get('page','1'))
    except Exception:
        page = 1
    try:
        foods = paginator.page(page)
    except(InvalidPage,EmptyPage):
        foods = Paginator.page(paginator.num_pages)


    #user data
    profile = request.user.username
    return render(request,'index.html',{'category':c_page,'foods':foods, "profile":profile})

@customer_required
def hotels(request,h_slug):
    if request.method == 'POST':
        # Process the form submission
        user = request.user
        hotel_id = request.POST.get('hotel')
        hotel = get_object_or_404(Hotel, id=hotel_id)
        
        # Create OrderItem instance
        order_item = OrderItem.objects.create(
            user=user,
            hotel=hotel,
            del_charge=20,
            total_amount=0,  # Placeholder, to be calculated
            active=True
        )
        
        # Collect all OrderFood objects from the POST data
        total_amount = 0
        for key, value in request.POST.items():
            if key.startswith('food_quantity_'):
                food_id = key.split('_')[-1]
                quantity = int(value)
                
                if quantity > 0:
                    food = get_object_or_404(Food, id=food_id)
                    order_food = OrderFood.objects.create(
                        food=food,
                        quantity=quantity
                    )
                    order_item.o_food.add(order_food)
                    total_amount += order_food.q_total()
        
        # Update the total_amount field
        order_item.total_amount = total_amount + order_item.del_charge
        order_item.save()

        # Redirect to the order summary or confirmation page
        return redirect('user_app:orderuser', or_id=order_item.id)
    else:
        hotel = get_object_or_404(Hotel, slug=h_slug)
        foods = hotel.foods.all()
        return render(request, 'hotel.html', {"hotel": hotel, 'foods': foods})
   


def foodfind(request,f_slug,c_slug):
    food = get_object_or_404(Food,slug=f_slug)
    hotels_of_fd = Hotel.objects.all().filter(foods=food)
    

    return render(request,'foodfind.html',{'foods':food,'ht':hotels_of_fd})

@customer_required
def order_user(request, or_id):  # sourcery skip: avoid-builtin-shadow
    order = get_object_or_404(OrderItem, id=or_id)
    if request.method == 'POST':
        name = request.POST.get('customer')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        notes = request.POST.get('notes')
        country = request.POST.get('country')
        zip = request.POST.get('zip')
        payment_type = request.POST.get('payment')
        payment = payment_type == "Online Pay"
        otp = random.randint(1000,9999)

        try:
            u_order = UserOrder.objects.create(
                customer=name, address=address, mobile=mobile,
                notes=notes, country=country, zip=zip,status='pending',otp=otp, payment=payment,
                payment_type=payment_type, delivery_b=None, order=order
            )
            u_order.save()
            return HttpResponse('success')
        except Exception as e:
            return HttpResponse(f"Can't make orders: {e}")
        
    return render(request,'order.html')

@customer_required
def order_view(request):
   
        
    user_orders = UserOrder.objects.filter(order__user=request.user)
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
    
    return render(request, 'order_view.html', context)

@customer_required
def order(request,o_id):
    order = UserOrder.objects.get(id=o_id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    if request.method == 'POST':
        order.delete()
        return redirect('user_app:home')
   
    return render(request,'order_pending.html',{'order':order,'foods':foods,'earn':earn})

@customer_required
def order_confirm(request,o_id):
    order = UserOrder.objects.get(id=o_id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    d_b = DelUser.objects.get(id=order.delivery_b)
    
   
    return render(request,'order_confirm.html',{'order':order,'foods':foods,'earn':earn,'d_b':d_b})
   

@customer_required
def setting(request):  # sourcery skip: extract-duplicate-method
    try:
        usr_profile = Customer.objects.get(user=request.user)
        is_new_profile = False
    except Customer.DoesNotExist:
        usr_profile = Customer(user=request.user)
        is_new_profile = True

    if request.method == 'POST':
        if 'image' in request.FILES:
            usr_profile.img = request.FILES['image']
        usr_profile.desc = request.POST.get('desc', usr_profile.desc)
        usr_profile.location = request.POST.get('location', usr_profile.location)
        usr_profile.name = request.POST.get('name', usr_profile.name)
        contact = request.POST.get('contact', usr_profile.contact)

        if is_new_profile: # Automatically generate a slug
            usr_profile.slug = slugify(usr_profile.name)  
            
        
        usr_profile.contact = contact
        usr_profile.save()
        return redirect('user_app:home')  # Redirect to the same page to avoid re-submission
    return render(request, 'profile.html', {'user_profile': usr_profile, 'is_new_profile': is_new_profile})
