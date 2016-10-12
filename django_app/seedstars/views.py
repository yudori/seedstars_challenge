from django.shortcuts import render
from django.http import HttpResponse

from .models import Person


def index(request):
    return render(request, 'seedstars/index.html', {})


def add(request):
    context = {}
    if request.method == 'POST':
        person = Person(email=request.POST['email'],
                        name=request.POST['name'])
        person.save()
        context = { 'success_message' : "Record successfully added!"}
    return render(request, 'seedstars/add.html', context)


def list(request):
    person_list = Person.objects.all()
    context = {'persons' : person_list}
    return render(request, 'seedstars/list.html', context)