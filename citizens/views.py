from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .forms import CitizenForm
from .models import AccessToken

def show(request, token):
    if request.method == "GET":
        token_object = AccessToken.objects.get(token=token)
        return render(request, "citizens/show.html", {"citizen": token_object.citizen})

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