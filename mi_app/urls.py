from django.urls import path
##from .views import hola, listar_productos, layout, herencia
from mi_app import views

urlpatterns = [
    path("", views.hola, name="hola"),
    path("productos/", views.listar_productos, name="lista_productos"),
    path("layout/", views.layout, name="layout"),
    path("herencia/", views.herencia, name="herencia"),
]
