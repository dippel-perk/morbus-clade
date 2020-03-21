from django.urls import path, include
from .views import *

urlpatterns = [
    path('detail/<int:pk>', citizen_detail, name='detail'),
    path('show/<str:token>', show, name='citizen-show'),
    path('create', create, name='citizen-create'),

    path('show/<str:token>/contacts/add', add_contact_person, name='citizen-add-contact-person'),
]
