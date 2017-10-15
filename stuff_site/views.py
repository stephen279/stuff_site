#from django.http import HttpResponse
from django.shortcuts import render


def Hello_World(request):
    return render(request, 'home.html', )