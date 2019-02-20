from django.urls import path
from django.contrib import admin
from count import views

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name="count")
]
