from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def test():
    return HttpResponse("This is a Test")