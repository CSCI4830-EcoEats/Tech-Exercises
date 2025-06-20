from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('new/', views.person_create, name='person_create'),
    path('edit/<int:pk>/', views.person_update, name='person_update'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),
]
