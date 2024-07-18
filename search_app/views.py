from django.shortcuts import render
from django.db.models import Q
from hotel_app.models import Category, Food, Hotel

# Create your views here.


def search(request):
    foods = None
    ht = None
    ct = None
    query = None
    if 'q' in request.GET:
        
        query = request.GET.get('q').capitalize()
        
        foods = Food.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query ))
        ht = Hotel.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
        ct = Category.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    

    
    return render(request, 'search.html',{'query':query,'food':foods,'ht':ht,'ct':ct})




