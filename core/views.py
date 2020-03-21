from django.shortcuts import render
from health.models import User


def home(request):
    stations = User.objects.all()
    return render(request, "core/home.html", {'stations': stations})


def about_us(request):
    return render(request, "core/about_us.html")