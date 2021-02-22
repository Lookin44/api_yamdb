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


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        u = request.user
        return (obj.author == request.user or
                u.role == User.RoleUser.ADMIN or
                u.role == User.RoleUser.MODERATOR)


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        u = request.user
        return (obj.author == request.user or
                u.role == User.RoleUser.ADMIN or
                u.role == User.RoleUser.MODERATOR)
