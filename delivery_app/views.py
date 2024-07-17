from django.shortcuts import redirect, render,get_object_or_404
from hotel_app.models import Hotel, Category,Food
from .models import DelUser
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from authenticate_users.decorators import delivery_user_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@delivery_user_required
def home(request):
    return render(request, 'd_home.html')


@delivery_user_required
def setting(request):  # sourcery skip: extract-duplicate-method
    del_profile = DelUser.objects.get(user=request.user)
    if request.method == 'POST':
        

        if request.FILES.get('image') is None:
           Image = del_profile.img
           desc =request.POST['desc']
           Location = request.POST['location']
           name = request.POST['name']
           
           contact = request.POST['contact']



           del_profile.img = Image
           del_profile.desc = desc
           del_profile.location = Location
           del_profile.name =name
           del_profile.contact = contact
           del_profile.save()

          

        if request.FILES.get('image') != None:
            Image = request.FILES.get('img')
            name = request.POST['name']
            contact = request.POST['contact']



            del_profile.img = Image
            del_profile.desc = desc
            del_profile.location = Location
            del_profile.name =desc
            del_profile.contact = contact
            del_profile.save()

            

        return redirect('delivery_app:setting')
        
    return render(request, 'd_profile.html', {'user_profile':del_profile})