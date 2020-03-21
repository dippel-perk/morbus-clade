from django.urls import path, include
from .views import *

urlpatterns = [
    path('home', home, name='citizen-home'),
    path('show/<str:token>', show, name='citizen-show'),
    path('create', create, name='citizen-create'),
]
