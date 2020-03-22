from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about_us, name='about-us'),
    path('description', description, name='description')
]
