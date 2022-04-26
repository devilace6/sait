from django.urls import path
from django.contrib import admin
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('user_profile/', profile, name='users-profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)