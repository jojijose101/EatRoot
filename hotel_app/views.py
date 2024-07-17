from django.shortcuts import redirect, render,get_object_or_404
from authenticate_users.decorators import hotel_user_required
from hotel_app.models import Hotel, Category,Food

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models  import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@hotel_user_required
def home(request):
    return render(request, 'h_home.html')


@hotel_user_required
def setting(request):  # sourcery skip: extract-duplicate-method
    hotel_profile = Hotel.objects.get(user=request.user)
    if request.method == 'POST':
        

        if request.FILES.get('image') is None:
           Image = hotel_profile.img
           desc =request.POST['desc']
           Location = request.POST['location']
           name = request.POST['name']
           email = request.POST['email']
           contact = request.POST['contact']



           hotel_profile.img = Image
           hotel_profile.desc = desc
           hotel_profile.location = Location
           hotel_profile.name =name
           hotel_profile.email = email
           hotel_profile.contact = contact
           hotel_profile.save()

          

        if request.FILES.get('image') != None:
            Image = request.FILES.get('img')
            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']



            hotel_profile.img = Image
            hotel_profile.desc = desc
            hotel_profile.location = Location
            hotel_profile.name =desc
            hotel_profile.email = email
            hotel_profile.contact = contact
            hotel_profile.save()

            

        return redirect('hotel_app:setting')
        
    return render(request, 'h_profile.html', {'user_profile':hotel_profile})



