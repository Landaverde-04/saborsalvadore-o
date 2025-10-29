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
from ModuloTipicos import views
from django.http import HttpResponse

def robots_txt(request):
    content = "User-agent: *\nAllow: /\nSitemap: https://saborsalvadore-o.onrender.com/sitemap.xml"
    return HttpResponse(content, content_type="text/plain")

urlpatterns = [
    path("robots.txt", robots_txt),
    path('admin/', admin.site.urls),
    path('', views.lista_tipicos, name='inicio'),
    path('tipicos/', include('ModuloTipicos.urls')),
      # Ruta para la página de inicio
]