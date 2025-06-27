from django.urls import path
from .views import hello_EcoEats, hello_world, hello_komlan

urlpatterns = [
    path('', hello_EcoEats, name='hello_EcoEat'),
    path('hello', hello_world, name='hello_world'),
    path('komlan', hello_komlan, name='hello_komlan'),
]
