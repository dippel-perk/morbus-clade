from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from .forms import CitizenForm, ContactPersonForm
from .models import AccessToken, Citizen
from health.models import User
from django.contrib import messages
from datetime import datetime, timedelta
from health.models import Test


def show(request, token):
    if request.method == "GET":
        token_object = AccessToken.objects.get(token=token)
        return render(request, "citizens/show.html", {"citizen": token_object.citizen, "token": token})
    return HttpResponseNotFound()


def citizen_detail(request, token):
    if request.method == "GET":
        token_object = get_object_or_404(AccessToken, token=token)
        contact_persons = citizen.contact_persons.order_by('last_contact')
        try:
            if token_object.citizen.test and token_object.citizen.test.is_positive:
                return render(request, 'citizens/detail.html', {'citizen': token_object.citizen, 'token_based': True, 'contact_persons': contact_persons})
            else:
                return redirect('citizen-show', token=token)
        except Test.DoesNotExist:
            return HttpResponseNotFound()
    return HttpResponseNotFound()


def create(request):
    if request.method == "POST":
        form = CitizenForm(request.POST)
        if form.is_valid():
            citizen = form.save()

            read_token = AccessToken(citizen=citizen)
            read_token.save()

            return redirect('citizen-show', token=read_token.token)
    else:
        form = CitizenForm()
    return render(request, 'citizens/create.html', {'form': form})


def add_contact_person(request, token):
    token_object = get_object_or_404(AccessToken, token=token)

    try:

        if token_object.citizen and token_object.citizen.test and token_object.citizen.test.is_positive:
            if request.method == "POST":
                form = ContactPersonForm(request.POST)
                if form.is_valid():
                    contact_person = form.save(commit=False)
                    contact_person.citizen = token_object.citizen
                    contact_person.save()

                    messages.success(request, "Die Kontaktperson erfolgreich hinzugefügt.")
                    return redirect('detail', token=token_object.token)
            else:
                form = ContactPersonForm()

            min_date = (token_object.citizen.test.created_at - timedelta(days=7)).strftime("%Y-%m-%d")
            max_date = token_object.citizen.test.created_at.strftime("%Y-%m-%d")

            return render(request, 'citizens/contact_persons/create.html',
                          {'form': form, 'min_date': min_date, 'max_date': max_date})

        return HttpResponseNotFound()
    except Test.DoesNotExist:
        return HttpResponseNotFound()
