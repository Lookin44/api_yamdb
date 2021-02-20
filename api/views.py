from rest_framework import filters, mixins, viewsets, permissions

from .models import Category
from .serializers import CategorySerializer


class IsAdminOrReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == 'GET':
            return True

        return request.user.is_authenticated


class CategoryViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnlyPermission]
