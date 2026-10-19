
from django.contrib import admin
from .models import Sucursal, PerfilUsuario, Incidencia, Seguimiento


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("clave", "nombre", "activa")
    search_fields = ("clave", "nombre")
    list_filter = ("activa",)


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "rol", "sucursal")
    list_filter = ("rol", "sucursal")
    search_fields = ("usuario__username", "usuario__email")


class SeguimientoInline(admin.TabularInline):
    model = Seguimiento
    extra = 0
    readonly_fields = ("usuario", "comentario", "creado_en")


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = (
        "folio",
        "sucursal",
        "titulo",
        "tipo",
        "prioridad",
        "estado",
        "responsable",
        "creado_en",
    )
    list_filter = ("sucursal", "tipo", "prioridad", "estado")
    search_fields = ("folio", "titulo", "descripcion")
    readonly_fields = (
        "folio",
        "creado_en",
        "actualizado_en",
        "resuelto_en",
    )
    inlines = [SeguimientoInline]


@admin.register(Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ("incidencia", "usuario", "creado_en")
    search_fields = ("incidencia__folio", "comentario")
    readonly_fields = ("creado_en",)
