import pandas as pd
import requests

def procesar_excel_examenes(archivo, usuario):
    """
    Procesa un archivo Excel cargado y crea registros de ResultadoExamen.
    """
    from .models import ResultadoExamen, CatalogoExamen

    try:
        df = pd.read_excel(archivo)
    except Exception as e:
        return 0, [f"Error al leer Excel: {str(e)}"]

    errores = []
    creados = 0
    
    for index, row in df.iterrows():
        try:
            # Búsqueda insensible a mayúsculas/minúsculas
            catalogo = CatalogoExamen.objects.get(nombre__iexact=row['Examen'])
            
            ResultadoExamen.objects.create(
                paciente=usuario,
                examen_tipo=catalogo,
                valor=row['Valor'],
                fecha_examen=row['Fecha']
            )
            creados += 1
        except CatalogoExamen.DoesNotExist:
            errores.append(f"Fila {index+2}: El examen '{row['Examen']}' no existe en el catálogo.")
        except Exception as e:
            errores.append(f"Fila {index+2}: {str(e)}")
            
    return creados, errores


def consultar_faker_api_recomendacion(termino):
    """
    Sustituimos a MedlinePlus usando fakerapi
    """
    url = "https://fakerapi.it/api/v1/texts?_quantity=1&_characters=200"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data['data']:
                texto_simulado = data['data'][0]['content']
                return f"RECOMENDACIÓN PREVENTIVA PARA {termino.upper()}:\n{texto_simulado}"
        
        return f"Nota: Se recomienda monitorear sus niveles de {termino} con un profesional."
    
    except Exception as e:
        print(f"Error al conectar con FakerAPI: {e}")
        return f"Consulte a su médico para una interpretación detallada de sus niveles de {termino}."