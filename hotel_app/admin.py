from django.contrib import admin

from hotel_app.models import Category, Food, Hotel


# Register your models here.
class CategoryForm(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryForm)


class HotelForm(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Hotel,HotelForm)

class FoodForm(admin.ModelAdmin):
    list_display = ['name','price','available','updated','created']
    list_editable = ['price','available',]
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Food,FoodForm)
