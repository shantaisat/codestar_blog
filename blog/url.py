from django.urls import path
from . import views

urlpatterns = [
    path('', my_blog, name='blog'),
]