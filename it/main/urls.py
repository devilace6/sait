from django.urls import path
from . import  views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='home'),
    path('category', views.category, name = 'category'),
    path('about', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)