from django.urls import path
from . import  views
import include

urlpatterns = [
    path('', views.news_home, name ='news_home'),
    path('create', views.create, name='create'),
    path('<slug:slug>', views.NewsDetail.as_view(), name='news_detail'),
    path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
]