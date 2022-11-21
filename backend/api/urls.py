from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_home),
    #path("", views.api_home2),
]