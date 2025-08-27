from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Bem-vindo à página de Fotos de Viagens!</h1>")
# Create your views here.
