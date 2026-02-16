from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExamenViewSet, exportar_reporte_excel

router = DefaultRouter()
router.register(r'gestion-examenes', ExamenViewSet)

urlpatterns = [
    path('reporte-excel/<int:paciente_id>/', exportar_reporte_excel, name='reporte_excel'),
    path('', include(router.urls)),
]