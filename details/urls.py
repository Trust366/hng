from django.urls import path 
from rest_framework.routers import DefaultRouter
from . import apis as views 

urlpatterns = [
    path('', views.DetailView.as_view()),
]

