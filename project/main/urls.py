from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('time/<int:id>/', views.time, name='time_url'),
    path('basket/<int:id>/', views.basket, name='basket_url'),
]