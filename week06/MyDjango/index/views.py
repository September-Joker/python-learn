from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Hello Django!')


def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def myyear(request, year):
    return render(request, 'yearview.html')
