# Exadesan: Ecosistema de Salud Preventiva
Exadesan es una plataforma avanzada de gestión clínica desarrollada en Django 6.0. Su objetivo es transformar los resultados de laboratorio en información accionable, utilizando análisis de rangos automáticos y recomendaciones preventivas inteligentes.

# Capacidades del Sistema
## Dashboards Especializados:
- Panel Administrativo: Control total de la población de usuarios y gestión del catálogo médico (rangos de referencia).
- Panel Médico: Vista global de estadísticas de salud, detección de pacientes en riesgo y gestión de consultas.
- Portal del Paciente: Visualización histórica de resultados, acceso a documentos PDF y seguimiento gráfico.

## Inteligencia de Datos:
- Clasificación Automática: Los resultados se categorizan como NORMAL, ALTO o BAJO al instante.
- Alertas Preventivas: Generación de correos automáticos ante anomalías, integrando recomendaciones vía FakerAPI.

## Visualización y Análisis:
- Gráficos Dinámicos: Seguimiento de tendencias (ej. Glucosa) mediante gráficos integrados que muestran la evolución temporal frente a los rangos permitidos.

## Herramientas de Exportación Profesional:
- PDF Clínico: Generación de informes dinámicos con ReportLab, incluyendo formato de tabla y colores de riesgo.
- Excel Avanzado: Exportación de reportes con estilos, celdas coloreadas y auto-ajuste de columnas con OpenPyXL.

## Integración y API:
- Carga Masiva: Capacidad de procesar archivos Excel para la ingesta de grandes volúmenes de datos.
- API RESTful: Endpoints configurados para búsquedas, filtros y operaciones CRUD de exámenes.

# Stack Tecnológico
- Core: Python 3.x, Django 6.0
- Reporting: ReportLab (PDF), OpenPyXL & Pandas (Excel)
- API: Django Rest Framework
- Frontend: Django Templates, AJAX (JSON responses), JavaScript para gráficos.
- Seguridad: python-dotenv para protección de secretos.

# Flujo Administrativo
- Mantenimiento de Usuarios: El administrador crea perfiles (Médico/Paciente) y asigna roles.
- Catálogo: Se deben cargar los exámenes clínicos base (ej. Hemoglobina) definiendo sus rangos min/max.

# Flujo del Paciente
- Carga de Examen: El paciente o médico sube el resultado.
- Consulta: El paciente recibe un correo si su valor es de riesgo.
- Descarga: Puede generar su reporte en PDF o Excel desde su panel personal.

# Gráficos de Evolución
El sistema agrupa los resultados por tipo de examen y genera etiquetas temporales para que el usuario visualice si su salud está mejorando o requiere intervención.
