from django.urls import path
from . import  views
from django.conf.urls import url, include

urlpatterns = [
    path('', views.index, name ='home'),
    path('category', views.category, name = 'category'),
    path('about', views.about, name='about'),
]