from rest_framework import permissions

from users.models import RoleUser


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if not user.is_authenticated:
            return False

        return user.role == RoleUser.ADMIN or user.is_superuser


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        return (obj.author == request.user
                or user.role == RoleUser.ADMIN
                or user.role == RoleUser.MODERATOR)
