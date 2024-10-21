from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('time/<int:id>/', views.time, name='time_url'),
    path('student/<int:id>/', views.student, name='student_url'),
]