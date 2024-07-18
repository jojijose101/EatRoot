from django.shortcuts import redirect, render,get_object_or_404
from hotel_app.models import Hotel, Category,Food
from .models import DelUser
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.template.defaultfilters import slugify
from authenticate_users.decorators import delivery_user_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@delivery_user_required
def home(request):
    return render(request, 'd_home.html')


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

