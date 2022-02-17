from django.contrib import admin
from .models import Articles, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Articles)

prepopulated_fields = {"slug": ("title")}