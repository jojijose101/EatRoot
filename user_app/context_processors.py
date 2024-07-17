from hotel_app.models import Hotel, Category
from .models import OrderItem

def links(request):
    h_link = Hotel.objects.all()
    c_link = Category.objects.all()
    return dict(h_link=h_link,c_link=c_link)

