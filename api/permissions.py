from rest_framework import permissions


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_authenticated or request.user.is_superuser
