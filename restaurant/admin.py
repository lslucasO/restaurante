from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    ...

class MealAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'created_at',
        'is_published',
        'author',
        'category',
    ]
    
    search_fields = [
        'id',
        'title',
        'description',
        'created_at',
        'slug',
        'category'
    ]
    
    list_display_links = [
        'title',
        'created_at'
    ]

    list_per_page = 10
    
    list_editable = [
        'is_published'
    ]
    
    ordering = [
        '-id'
    ]
    
    prepopulated_fields = {
        'slug': ('title',)
    }
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal, MealAdmin)