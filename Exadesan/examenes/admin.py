from django.contrib import admin
from .models import Perfil, CatalogoExamen, ResultadoExamen

@admin.register(CatalogoExamen)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rango_min', 'rango_max', 'unidad_medida')

@admin.register(ResultadoExamen)
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'examen_tipo', 'valor', 'nivel_riesgo', 'fecha_examen')
    list_filter = ('nivel_riesgo', 'examen_tipo')
    search_fields = ('paciente__username', 'examen_tipo__nombre')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono')