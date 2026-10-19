
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nueva/", views.nueva_incidencia, name="nueva_incidencia"),
    path("exportar/", views.exportar_excel, name="exportar_excel"),
]
