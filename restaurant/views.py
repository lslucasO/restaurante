from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *


def home(request):
    meals = Meal.objects.filter(
        is_published=True,
    ).order_by('-id')
    
    context = {
        'meals': meals,
        'title': 'Home'
    }
    
    return render(request, 'global/partials/home.html', context)


def meal(request, id):
    meals = get_object_or_404(
        Meal,
        pk = id,
        is_published = True
    )
    
    context = {
        'title': 'Meal',
        'meal': meals
    }
    
    return render(request, 'restaurant/pages/meal-page.html', context)


def category_view(request, category):
    meals = Meal.objects.filter(
        category=category,
        is_published=True
    )
    
    context = {
        'meals': meals,
        'title': category
    }
    
    return render(request, 'restaurant/pages/category_view.html', context)


def category_list(request):
    return 