from django.urls import path
from .views import hello_EcoEats, hello_world

urlpatterns = [
    path('', hello_EcoEats, name='hello_EcoEat'),
    path('/hello', hello_world, name='hello_world'),
]
