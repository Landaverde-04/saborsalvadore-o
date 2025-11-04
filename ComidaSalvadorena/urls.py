"""
URL configuration for ComidaSalvadoreña project.

Incluye rutas para servir archivos físicos robots.txt y sitemap.xml
directamente desde la raíz del proyecto.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse, FileResponse
from ModuloTipicos import views
from django.conf import settings
import os


# --- robots.txt físico ---
def robots_txt(request):
    robots_path = os.path.join(settings.BASE_DIR, "robots.txt")
    if not os.path.exists(robots_path):
        # Respaldo si el archivo no existe
        default_content = (
            "User-agent: *\n"
            "Allow: /\n"
            f"Sitemap: https://saborsalvadore-o.onrender.com/sitemap.xml"
        )
        return HttpResponse(default_content, content_type="text/plain")

    # Devuelve el archivo físico
    return FileResponse(open(robots_path, "rb"), content_type="text/plain")


# --- sitemap.xml físico ---
def sitemap_xml(request):
    sitemap_path = os.path.join(settings.BASE_DIR, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        return HttpResponse(
            "Sitemap no encontrado.", content_type="text/plain", status=404
        )
    return FileResponse(open(sitemap_path, "rb"), content_type="application/xml")


# --- verificación Google Search Console ---
def google_verify(request):
    return HttpResponse(
        "google-site-verification: google669a5b739326ea1b.html",
        content_type="text/plain",
    )


# --- URLs principales ---
urlpatterns = [
    # Archivos raíz
    path("robots.txt", robots_txt),
    path("sitemap.xml", sitemap_xml),
    path("google669a5b739326ea1b.html", google_verify),

    # Administración y contenido
    path("admin/", admin.site.urls),
    path("", views.lista_tipicos, name="inicio"),
    path("tipicos/", include("ModuloTipicos.urls")),
]
