# Django_clase2
Modulo6 - día 2

# PASOS: 
## crear entorno 
python -m venv entorno 

## activar entorno 
source entorno/bin/activate  

## Instala Djgango 
pip install django 
pip install -r requirements.txt

## actualización pip 
pip install --upgrade pip

## Levanta proyecto 
django-admin startproject proyecto .

## correr servidor 
python manage.py runserver 

## Migraciones 
python manage.py makemigrations 
python manage.py migrate

## Crear super usuario
python manage.py createsuperuser

## Para habilitar host
En setting.py - bajo ALLOWED_HOSTS = [] (linea 28)

CSRF_TRUSTED_ORIGINS = [
    "https://localhost:8000",
]

## Crear app 
python manage.py startapp "NOMBRE"

## Crear archivo ulrs.py en app
## Agregar app a setting.py del proyecto (backend) en linea 36
INSTALLED_APPS = [
    ...
    "mi_app",
]

## En urls.py del proyecto, agregar un archivo de rutas externo:
linea 19 (agregar include): from django.urls import path, include
linea 23: path("", include("mi_app.urls")),

## Modificar urls.py de la app (mi_app)
from django.urls import path

urlpatterns = [
    "POR AGREGAR"
]

## modificar views.py de app agregando función:
def hola(request):
    return render(request, "Hola.html")

## agregar la ruta en urls.py de la app
from django.urls import path
from .views import hola

urlpatterns = [
    path("hola/", hola)
]

## Crear carpeta templates fuera.
## Crear un archivo hola.html
## Modificar setting.py linea 61 "DIR":
"DIRS": [BASE_DIR / "templates"],

## Modificar html


## Para guardar imagenes en carpeta aparte: agregar en setting.py
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
## Luego en urls del proyecto agregar:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
