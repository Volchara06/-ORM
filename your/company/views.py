from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, world! This is the company app.</h1>")

# Create your views here.
