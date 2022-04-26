from django.contrib import admin
from .models import Articles, Category, Comments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Articles)

prepopulated_fields = {"slug": ("title")}

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'create_date')
