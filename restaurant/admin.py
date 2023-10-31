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
    
    list_display_links = [
        'title',
        'created_at'
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal, MealAdmin)