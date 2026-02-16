from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Perfil(models.Model):
    ROLES = (
        ('PACIENTE', 'Paciente'),
        ('MEDICO', 'Médico'),
        ('ADMIN', 'Administrador'),
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    rol = models.CharField(max_length=20, choices=ROLES, default='PACIENTE')
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"

class CatalogoExamen(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    unidad_medida = models.CharField(max_length=20)
    rango_min = models.DecimalField(max_digits=10, decimal_places=2)
    rango_max = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_referencia = models.CharField(max_length=50, help_text="Código médico o término de búsqueda")

    def __str__(self):
        return self.nombre

class TipoExamen(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=50)
    rango_bajo = models.FloatField()
    rango_normal = models.FloatField()
    rango_alto = models.FloatField()

    def __str__(self):
        return self.nombre

class ResultadoExamen(models.Model):
    RIESGO_CHOICES = (
        ('BAJO', 'Bajo'),
        ('NORMAL', 'Normal'),
        ('ALTO', 'Alto'),
    )

    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    examen_tipo = models.ForeignKey(CatalogoExamen, on_delete=models.CASCADE)
    fecha_examen = models.DateField()
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    nivel_riesgo = models.CharField(max_length=20)
    observaciones_medline = models.TextField(blank=True, null=True)

    documento_pdf = models.FileField(
        upload_to='examenes_adjuntos/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png'])],
        null=True, blank=True
    )

    class Meta:
        ordering = ['-fecha_examen']

    def save(self, *args, **kwargs):
        if self.valor < self.examen_tipo.rango_min:
            self.nivel_riesgo = 'BAJO'
        elif self.valor > self.examen_tipo.rango_max:
            self.nivel_riesgo = 'ALTO'
        else:
            self.nivel_riesgo = 'NORMAL'

        if self.nivel_riesgo != 'NORMAL' and not self.observaciones_medline:
            from .services import consultar_faker_api_recomendacion
            self.observaciones_medline = consultar_faker_api_recomendacion(self.examen_tipo.nombre)

        super().save(*args, **kwargs)

        # Alerta por correo
        if self.nivel_riesgo != 'NORMAL':
            try:
                from .alerts import enviar_alerta_riesgo
                enviar_alerta_riesgo(self)
            except Exception as e:
                print(f"Error al intentar enviar la alerta: {e}")

    def __str__(self):
        return f"{self.examen_tipo.nombre}: {self.valor} ({self.nivel_riesgo})"