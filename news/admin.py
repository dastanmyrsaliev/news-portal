from django.contrib import admin

from .models import Category, News


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'category', 
        'published_at',
    )
    list_display_links = ('id', 'title')
    list_filter = ('category', 'published_at')
    search_fields = ('title', 'content', 'category__name')
    ordering = ('-published_at',)
