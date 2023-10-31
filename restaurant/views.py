from django.shortcuts import render
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