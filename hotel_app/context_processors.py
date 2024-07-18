from .models import Hotel


def links(request):
    try:
       hotel_link = Hotel.objects.get(user=request.user)
    except:
        hotel_link = None
    return dict(hotel_link=hotel_link)