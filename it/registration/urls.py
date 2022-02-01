from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name = 'login'),
    path('registration', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
]