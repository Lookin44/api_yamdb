from rest_framework import permissions

from users.models import User


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        u = request.user
        if not u.is_authenticated:
            return False

        return u.role == User.RoleUser.ADMIN or u.is_superuser
