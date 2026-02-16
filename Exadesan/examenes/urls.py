p_name = 'examenes'

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "examenes"

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.redirect_dashboard, name='redirect_dashboard'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/medico/', views.dashboard_medico, name='dashboard_medico'),
    path('dashboard/paciente/', views.dashboard_paciente, name='dashboard_paciente'),

    # Exámenes
    path('lista-examenes/', views.lista_examenes, name='lista_examenes'),
    path('cargar-examen/', views.cargar_examen, name='cargar_examen'),
    path('examen/<int:examen_id>/', views.ver_examen, name='ver_examen'),
    path('examen/<int:examen_id>/descargar/', views.descargar_examen, name='descargar_examen'),

    # Pacientes
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    # Cambia views.mi_vista por views.exportar_reporte_excel
    path('exportar/<int:reporte_id>/', views.exportar_reporte_excel, name='exportar_reporte_excel_con_id'),
    # Estadísticas
    path('estadisticas/', views.estadisticas_medico, name='estadisticas_medico'),

    # Catálogo
    path('catalogo/', views.ver_catalogo, name='ver_catalogo'),
    path('catalogo/crear/', views.crear_catalogo_examen, name='catalogo_crear'),
    path('catalogo/editar/<int:id>/', views.editar_catalogo_examen, name='catalogo_editar'),
    path('catalogo/eliminar/<int:id>/', views.eliminar_catalogo_examen, name='catalogo_eliminar'),

    # Usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path("usuarios/crear/", views.crear_usuario, name="crear_usuario"),
    path('usuarios/<int:usuario_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuario/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),
    path("usuarios/ajax/crear/", views.crear_usuario_ajax, name="crear_usuario_ajax"),

    # Otros
    path("grafico/glucosa/", views.grafico_glucosa, name="grafico_glucosa"),
    path('logout/', LogoutView.as_view(next_page='examenes:redirect_dashboard'), name='logout'),
    path('redirect-dashboard/', views.redirect_dashboard, name='redirect_dashboard'),
    path('dashboard/paciente/reportes/excel/', views.descargar_reportes_excel, name='descargar_reportes_excel'),
    path('dashboard/paciente/reportes/pdf/', views.descargar_reportes_pdf, name='descargar_reportes_pdf'),
]