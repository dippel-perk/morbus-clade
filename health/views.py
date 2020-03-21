from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .models import User, Test
from citizens.models import Citizen, AccessToken
from django.core import serializers


@login_required
def home(request):
    if request.user.is_health_department:
        citizens = Citizen.objects.all()
        citizens_json = serializers.serialize("json", citizens)
        return render(request, 'health/health_department/home.html', {'citizens': citizens_json})


# @login_required
def create_test(request):
    if request.method == "POST":
        token = get_object_or_404(AccessToken, token=request.POST.get("token", ""))
        citizen = token.citizen

        test_station = get_object_or_404(User, pk=4)
        laboratory = get_object_or_404(User, pk=7)

        test = Test(citizen=citizen, test_station=test_station, laboratory=laboratory)
        test.save()

        return redirect("citizen-show", token=token.token)

    return HttpResponseNotFound()


# @login_required
def update_test_result(request):
    if request.method == "POST":
        token = get_object_or_404(AccessToken, token=request.POST.get("token", ""))
        citizen = token.citizen

        if not citizen.test:
            return HttpResponseNotFound()

        result = int(request.POST.get("result", -1))
        choice = next((t for t in Test.RESULT_CHOICES if t[0] == result))

        if choice:
            citizen.test.result = choice[0]
            citizen.test.save()

        return redirect("citizen-show", token=token.token)

    return HttpResponseNotFound()
