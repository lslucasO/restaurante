from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from project import settings

app_name = 'restaurant'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
     path('meal-page/<int:id>', views.meal, name='meal-page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)