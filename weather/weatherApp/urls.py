from django.urls import path
from .views import addCity, deleteCity, index

urlpatterns = [
    path('', index, name = 'home'),
    path('addcity/', addCity, name = 'addcity'),
    path('delete_city/',deleteCity,name = 'delete_city'),    
]