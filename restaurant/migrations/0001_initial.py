# Generated by Django 4.2.6 on 2023-10-31 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('cover', models.ImageField(blank=True, default='', upload_to='shop/covers/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('avaliable_until', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.category')),
            ],
        ),
    ]