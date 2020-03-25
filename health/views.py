from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from .models import User, Test
from citizens.models import Citizen, AccessToken
from django.core import serializers
import json


@login_required
def home(request):
    if request.user.is_health_department:
        citizens = Citizen.objects.all()
        citizen_data = []
        for citizen in citizens:
            data = citizen.to_dict()
            data['id'] = citizen.pk
            status = 'Ausstehend'
            if hasattr(citizen, 'test'):
                if citizen.test.is_positive:
                    status = 'Positiv'
                elif citizen.test.is_negative:
                    status = 'Negativ'
            data["status"] = status
            citizen_data.append(data)
        citizens_json = json.dumps(citizen_data)
        return render(request, 'health/health_department/home.html', {'citizens': citizens_json})


@login_required
def evaluation(request):
    citizens = Citizen.objects.all()

    min_age = min((citizen.age for citizen in citizens))
    max_age = max((citizen.age for citizen in citizens))

    min_contact_person_count = min((citizen.contact_persons.count() for citizen in citizens))
    max_contact_person_count = max((citizen.contact_persons.count() for citizen in citizens))

    plots_data = {
        'proportion_chart': {
            'positive': 0,
            'negative': 0,
            'unknown': 0,
        },
        'ages_chart': {
            'ages': list(range(min_age, max_age + 1)),
            'positives': [0] * (max_age - min_age + 1),
            'negatives': [0] * (max_age - min_age + 1)
        },
        'contact_persons_chart': {
            'contact_person_counts': list(range(min_contact_person_count, max_contact_person_count + 1)),
            'citizens_with_cp_amounts': [0] * (max_contact_person_count - min_contact_person_count + 1)
        }
    }
    
    for citizen in citizens:

        age_index = plots_data['ages_chart']['ages'].index(citizen.age)
        contact_person_index = plots_data['contact_persons_chart']['contact_person_counts'].index(
            citizen.contact_persons.count())

        plots_data['contact_persons_chart']['citizens_with_cp_amounts'][contact_person_index] += 1

        if hasattr(citizen, 'test'):
            if citizen.test.is_positive:
                plots_data['proportion_chart']['positive'] += 1
                plots_data['ages_chart']['positives'][age_index] += 1
            elif citizen.test.is_negative:
                plots_data['proportion_chart']['negative'] += 1
                plots_data['ages_chart']['negatives'][age_index] += 1
            else:
                plots_data['proportion_chart']['unknown'] += 1

    return render(request, 'health/health_department/evaluation.html', plots_data)


@login_required
def citizen_detail_pk(request, pk):
    if request.method == "GET":
        citizen = get_object_or_404(Citizen, pk=pk)
        contact_persons = citizen.contact_persons.order_by('last_contact')
        return render(request, 'citizens/detail.html', {'citizen': citizen, 'contact_persons': contact_persons})
    return HttpResponseNotFound()


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

        redirect_adress = 'citizen-show'

        if choice:
            citizen.test.result = choice[0]
            citizen.test.save()

            if choice[0] == Test.POSITIVE:
                redirect_adress = 'detail'

        return redirect(redirect_adress, token=token.token)

    return HttpResponseNotFound()
