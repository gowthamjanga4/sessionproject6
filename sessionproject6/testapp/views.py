from django.shortcuts import render
from testapp.forms import *


# ADd your views here.

def name_view(request):
    name = NameForm()
    return render(request, 'testapp/name.html', {'name': name})


def age_view(request):
    name = request.GET['name']
    request.session['name'] = name
    age = AgeForm()
    return render(request, 'testapp/age.html', {'name': name, 'age': age})


def gf_view(request):
    name = request.session['name']
    age = request.GET['age']
    request.session['age'] = age
    gf = GfForm()
    return render(request, 'testapp/gf.html', {'name': name, 'gf': gf})


def results_view(request):
    gf = request.GET['gf']
    request.session['gf'] = gf
    return render(request, 'testapp/results.html', {'gf': gf})
