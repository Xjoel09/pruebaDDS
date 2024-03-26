
# En tu archivo views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# En tu archivo urls.py dentro de la aplicación "main"
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
]
