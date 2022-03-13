from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('user_profile/', profile, name='users-profile'),
]