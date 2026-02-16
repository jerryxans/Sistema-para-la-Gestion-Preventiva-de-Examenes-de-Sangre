# Manual de Usuario - Sistema Exadesan
Bienvenido a la guía oficial de Exadesan. Este sistema permite centralizar el control de salud preventiva, facilitando la comunicación entre el laboratorio, el médico y el paciente.

# 1 - Acceso al Sistema
Para ingresar a la plataforma, el administrador debe haber creado previamente su cuenta.
- Introduzca su Nombre de usuario y Contraseña.
- El sistema lo redirigirá automáticamente a su panel (Dashboard) según su rol: Administrador, Médico o Paciente.
> [!IMPORTANT]
> Si olvida su contraseña, por favor contacte al administrador del sistema médico.

# 2 - Módulo de Administrador
## Gestión de Usuarios
- Crear Usuarios: Desde el menú "Usuarios", puede registrar nuevos Médicos o Pacientes.
- Asignación de Roles: Al crear un usuario, es vital seleccionar el Rol correcto para que el sistema le otorgue los permisos adecuados.
- Edición/Eliminación: Permite actualizar teléfonos o correos electrónicos de los perfiles.
## Configuración del Catálogo
- Rangos de Referencia: Al registrar un examen (ej. Glucosa), debe definir el Rango Mínimo y Rango Máximo.
- Unidades: Especifique si es mg/dL, u/L, etc.

# 3 - Módulo de Médicos
Los médicos tienen una visión analítica de la población de pacientes.
- Lista de Pacientes: Permite ver a todos los pacientes registrados. Al hacer clic en uno, se visualiza su historial completo de exámenes.
- Estadísticas Globales: Visualización del estado de salud de la clínica (cuántos pacientes están en riesgo alto, normal o bajo).
- Carga de Resultados: El médico puede cargar los resultados de un paciente directamente seleccionando su nombre del listado.

# 4 - Módulo de Pacientes
El paciente es el centro del sistema.
## Mis Exámenes
- Visualización: El paciente puede ver una lista de todos sus exámenes realizados, ordenados por fecha.
- Alertas de Riesgo: Si un valor está fuera de rango, el sistema marcará el resultado con etiquetas de color. ALTO (rojo): Valor por encima del rango normal. BAJO (naranja): Valor por debajo del rango normal. NORMAL (verde): Valor dentro de los parámetros saludables.
## Descarga de Reportes
El sistema ofrece dos formas de llevarse la información:
- Reporte PDF: Un documento formal y estético listo para imprimir o enviar por WhatsApp a otro especialista.
- Reporte Excel: Una hoja de cálculo detallada para llevar un control personal de los datos.
## Gráficos de Evolución
En la sección de "Gráficos", el paciente puede seleccionar un examen (ej. Glucosa) y ver una línea de tiempo. Esto permite identificar si sus niveles están subiendo o bajando con el paso de los meses.

# 5 - Alertas Automatizadas
- Detección: Al guardar un examen, el sistema analiza el valor contra el catálogo.
- Recomendación API: Si hay riesgo, el sistema consulta automáticamente una base de datos médica (FakerAPI) para dar un consejo preventivo.
- Notificación: Se envía un correo electrónico inmediato al paciente con el detalle del resultado y la sugerencia médica.

> [!IMPORTANT]
> Aviso Legal: Exadesan es una herramienta de apoyo preventivo. Las recomendaciones automáticas no sustituyen el criterio clínico de un profesional de la salud.
