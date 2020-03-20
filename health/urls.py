from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import home

urlpatterns = [
    path('', home, name='health-home'),
    path('login', LoginView.as_view(template_name='health/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='health/logout.html'), name='logout'),

]
