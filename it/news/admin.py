from django.contrib import admin
from .models import Articles

admin.site.register(Articles)

prepopulated_fields = {"slug": ("title")}