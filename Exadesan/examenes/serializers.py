from rest_framework import serializers
from .models import ResultadoExamen

class ExamenSerializer(serializers.ModelSerializer):
    nombre_examen = serializers.ReadOnlyField(source='examen_tipo.nombre')
    
    class Meta:
        model = ResultadoExamen
        fields = ['id', 'paciente', 'nombre_examen', 'examen_tipo', 'valor', 'fecha_examen', 'nivel_riesgo']
