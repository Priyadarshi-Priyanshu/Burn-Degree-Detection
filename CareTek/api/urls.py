from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("", views.index, name="index"),
    path("burn_wound", views.burn_wound, name="burn_wound")
]
