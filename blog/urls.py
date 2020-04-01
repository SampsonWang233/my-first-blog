from django.urls import path
from . import views
import os
import django
os.environ.setdefault('DJANGO_SETTING_MODULE', 'mysite.settings')
django.setup()

urlpatterns = [
    path('', views.post_list, name='post_list'),
]