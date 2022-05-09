from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('ag/', views.adharGetView),
    path('ap/',views.adharPostView),
    path('ad/<int:pk>/', views.AdharInfo)
]