from rest_framework import permissions

class EsPropietarioOMedicoAdmin(permissions.BasePermission):
    """
    Permite acceso si:
    - El usuario es el dueño del examen (Paciente).
    - El usuario tiene rol Médico o Administrador.
    """

    def has_object_permission(self, request, view, obj):
        if obj.paciente == request.user:
            return True

        perfil = getattr(request.user, 'perfil', None)
        if perfil and perfil.rol in ['MEDICO', 'ADMIN']:
            return True

        if request.user.is_staff:
            return True

        return False