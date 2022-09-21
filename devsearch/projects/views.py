from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def projects(request):
    return HttpResponse('Here are our projects!')


def project(request, primary_key):
    return HttpResponse('Single Project' + ' ' + str(primary_key))