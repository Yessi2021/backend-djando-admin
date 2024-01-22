from rest_framework.permissions import BasePermission


class HasGroupPermission(BasePermission):

    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado
        if not request.user.is_authenticated:
            return False

        # Obtén los permisos requeridos para acceder a la vista
        required_permissions = getattr(view, "required_permissions", [])

        # Verifica si el usuario tiene todos los permisos requeridos
        return request.user.groups.filter(is_active=True, permissions__codename__in=required_permissions).exists()
