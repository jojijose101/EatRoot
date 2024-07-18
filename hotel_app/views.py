import re
from django.forms import ValidationError
from django.shortcuts import redirect, render,get_object_or_404
from authenticate_users.decorators import hotel_user_required
from hotel_app.models import Hotel, Category,Food
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@hotel_user_required
def home(request):
    return render(request, 'h_home.html')


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