from django.apps import AppConfig
def ready(self):
    import examenes.signals

class ExamenesConfig(AppConfig):
    name = 'examenes'
