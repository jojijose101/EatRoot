
from django.urls import path
from . import views

app_name = 'search_app'

urlpatterns = [
    path('search/search', views.search,name='search'),
    
]
