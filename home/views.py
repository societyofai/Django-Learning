from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print("inside index function")
    return HttpResponse("home page")

