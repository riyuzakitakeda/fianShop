from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('artwork/', views.artwork),
    path('profile/', views.profile),
    path('contact/', views.contact)
]