from django.shortcuts import render, redirect
from Entries.models import CreateCode

def index(request):
    return render(request, "main/main.html")

def dedication(request):
    return render(request, "main/dedication.html")