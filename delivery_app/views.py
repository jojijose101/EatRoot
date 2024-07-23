from django.shortcuts import redirect, render,get_object_or_404
from hotel_app.models import Hotel, Category,Food
from .models import DelUser
from user_app.models import UserOrder
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.template.defaultfilters import slugify
from authenticate_users.decorators import delivery_user_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@delivery_user_required
def home(request):
    
    d_b = DelUser.objects.get(user=request.user)
    orders = UserOrder.objects.filter(status='order_placed')
    o_f_d = UserOrder.objects.filter(status='out_for_delivery',delivery_b=d_b.id)
    completed = UserOrder.objects.filter(status='delivery_completed',delivery_b=d_b.id)
   



    return render(request, 'd_home.html',{'orders':orders,'o_f_d':o_f_d,'completed':completed})


@delivery_user_required
def setting(request):  # sourcery skip: extract-duplicate-method
    try:
        del_profile = DelUser.objects.get(user=request.user)
        is_new_profile = False
    except DelUser.DoesNotExist:
        del_profile = DelUser(user=request.user)
        is_new_profile = True

    if request.method == 'POST':
        if 'image' in request.FILES:
            del_profile.img = request.FILES['image']
        del_profile.desc = request.POST.get('desc', del_profile.desc)
        del_profile.location = request.POST.get('location', del_profile.location)
        del_profile.name = request.POST.get('name', del_profile.name)
        contact = request.POST.get('contact', del_profile.contact)

        if is_new_profile: # Automatically generate a slug
            del_profile.slug = slugify(del_profile.name)  
            
        
        del_profile.contact = contact
        del_profile.save()
        return redirect('delivery_app:home')  # Redirect to the same page to avoid re-submission
    return render(request, 'd_profile.html', {'user_profile': del_profile, 'is_new_profile': is_new_profile})

@delivery_user_required
def order_view(request,o_id):
    order = UserOrder.objects.get(id=o_id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    if request.method == 'POST':
        d_b = DelUser.objects.get(user=request.user)
        order.delivery_b = d_b.id
        order.status = 'out_for_delivery'
        order.save()
        return redirect('delivery_app:home')
   
    return render(request,'d_order_view.html',{'order':order,'foods':foods,'earn':earn})

@delivery_user_required
def confirm_order(request,o_id):
    d_b = DelUser.objects.get(user=request.user)
    order = UserOrder.objects.get(id=o_id,delivery_b = d_b.id)
    foods = order.order.o_food.all()
    earn = order.order.total_amount-20
    if request.method == 'POST':
        otp = request.POST.get('otp')
        print(type(otp))
        if int(otp) == order.otp:
            order.status = 'delivery_completed'
            d_b.earn += 20
            if order.payment == False:
                d_b.floating += order.order.total_amount
            d_b.save()

            order.save()
            return redirect('delivery_app:home')
        else:
            messages.error(request,"OTP doesn't match")
            return redirect('delivery_app:order_confirm',o_id)
   
    return render(request,'d_order_confirm.html',{'order':order,'foods':foods,'earn':earn})

@delivery_user_required
def earnings(request):
    earnings = DelUser.objects.get(user=request.user) 
    return render(request,'d_earnings.html',{'earnings':earnings})