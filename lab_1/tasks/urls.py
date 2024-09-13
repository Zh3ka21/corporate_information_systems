# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task2/', views.task2, name='task2'),
    
    path('task3/', views.task3, name='task3'),
    path('task3/success/', views.task3_success, name='task3_success'),
    path('task3/error/', views.task3_error, name='task3_error'),
    
    path('task4/', views.task4, name='task4'),
    path('task4/success/', views.task4_success, name='task4_success'),
    path('task4/error/', views.task4_error, name='task4_error'),
]
