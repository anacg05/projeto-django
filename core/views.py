from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Bem-vindo ao meu site Django!</h1>")
