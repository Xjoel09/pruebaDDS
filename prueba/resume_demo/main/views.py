from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def Comunidad(request):
    return render(request, "Comunidad.html")