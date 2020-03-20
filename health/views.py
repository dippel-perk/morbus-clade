from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def home(request):
    if request.user.is_health_department:
        return render(request, 'health/health_department/home.html')

