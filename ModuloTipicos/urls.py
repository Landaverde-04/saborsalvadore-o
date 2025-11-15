from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Esta ruta será accesible en /tipicos/
    path('', views.lista_tipicos, name='lista_tipicos'),

    # Ruta para el nuevo plato: /tipicos/nuevo/
    path('nuevo/', views.nuevo_plato, name='nuevo_plato'),

    # Ejemplo: una ruta para ver un detalle: /tipicos/pupusas/
    # path('<slug:nombre_plato>/', views.detalle_tipico, name='detalle_tipico'),
]