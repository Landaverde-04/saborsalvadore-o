"""
URL configuration for ComidaSalvadoreña project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Saborsalvadoreno/urls.py (Archivo de URLs del Proyecto Principal)

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye todas las rutas definidas en ModuloTipicos/urls.py
    # Serán accesibles bajo el prefijo '/tipicos/'
    path('tipicos/', include('ModuloTipicos.urls')),
    path('', views.lista_tipicos, name='home'),  # Ruta para la página de inicio
]