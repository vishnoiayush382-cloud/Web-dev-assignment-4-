from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('trains/', views.trains),
    path('passenger/', views.passenger),
    path('confirmation/', views.confirmation),
]