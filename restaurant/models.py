from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category


class Meal(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(unique=True, default='')
    description = models.TextField(max_length=165)
    price = models.FloatField()
    cover = models.ImageField(upload_to='shop/covers/%Y/%m/%d/', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    avaliable_until = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title