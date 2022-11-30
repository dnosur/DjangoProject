from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('Basket', views.Basket),
    path('SingIn', views.SingIn),
    path('SingUp', views.SingUp),
    path('Exit', views.Exit),
    path("Sort", views.Sort),
    path("Search", views.Search),
    path("Remove", views.Remove),
    path("AddProduct", views.AddProduct),
    path("Change", views.Change),
]