from django.shortcuts import render
from .models import Producto

# Create your views here.

def hola(request):
    return render(request, "hola.html")

def listar_productos(request):
    productos = Producto.objects.all()

    return render(request, "lista_de_productos.html", {"productos":productos})

def layout(request):
    return render(request, "mi_app/layout.html", {})

def herencia(request):
    return render(request, "mi_app/herencia.html", {})