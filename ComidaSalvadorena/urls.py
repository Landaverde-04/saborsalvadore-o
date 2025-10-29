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
from django.urls import path, include, reverse
from ModuloTipicos import views
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap

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

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['inicio']  # nombre de la ruta (name='inicio')

    def location(self, item):
        return reverse(item)

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns += [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

def google_verify(request):
    return HttpResponse("google-site-verification: google669a5b739326ea1b.html", content_type="text/plain")

urlpatterns += [
    path("google669a5b739326ea1b.html", google_verify),
]
