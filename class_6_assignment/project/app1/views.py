from django.shortcuts import HttpResponse, render
from django.urls import path, include

def home(request):
    return render(request, 'app1/app1.html')