from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    ...

class MealAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Meal, MealAdmin)