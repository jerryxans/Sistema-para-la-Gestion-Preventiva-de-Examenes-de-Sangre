from django.core.mail import send_mail
from django.conf import settings

def enviar_alerta_riesgo(resultado):
    """
    Envía una alerta por correo electrónico al detectar valores fuera de rango.
    Utiliza la recomendación obtenida de MedlinePlus Connect.
    """
    asunto = f"⚠️ ALERTA MÉDICA: {resultado.examen_tipo.nombre}"
    
    cuerpo = f"""
    Hola {resultado.paciente.username},
    
    Se ha detectado un valor fuera de rango en tu examen de {resultado.examen_tipo.nombre}.
    
    DATOS DEL EXAMEN:
    - Valor obtenido: {resultado.valor} {resultado.examen_tipo.unidad_medida}
    - Clasificación de Riesgo: {resultado.nivel_riesgo}
    - Fecha del examen: {resultado.fecha_examen}
    
    RECOMENDACIÓN PREVENTIVA (Basada en FakerAPI):
    {resultado.observaciones_medline if resultado.observaciones_medline else "Consulte a su médico para una interpretación detallada."}
    
    Por favor, consulta a tu médico de cabecera a la brevedad.
    ----------------------------------------------------------
    Este es un mensaje automático del Sistema de Gestión Preventiva.
    """
    
    try:
        # Intenta enviar el correo
        send_mail(
            asunto,
            cuerpo,
            settings.DEFAULT_FROM_EMAIL, # Remitente configurado en settings.py
            [resultado.paciente.email],   # correo del paciente
            fail_silently=False,
        )
        print(f"✅ ¡Correo enviado con éxito a {resultado.paciente.email}!")
        return True
    except Exception as e:
        print(f"❌ No se pudo enviar el correo: {e}")
        return False
