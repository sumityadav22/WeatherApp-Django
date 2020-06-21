from django.urls import path
from .views import addCity, index

urlpatterns = [
    path('', index, name = 'home'),
    path('addcity/', addCity, name = 'addcity'),
]