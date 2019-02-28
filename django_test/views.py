from django.shortcuts import render, redirect, reverse
from django_test.forms import PersonForm

def index(request):
    return render(request, 'index.html', {'form': PersonForm()})