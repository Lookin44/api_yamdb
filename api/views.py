import django_filters
from rest_framework import filters, mixins, viewsets, permissions

from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


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


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnlyPermission]


class TitleFilterBackend(django_filters.rest_framework.DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('name')
        if name:
            return queryset.filter(name__contains=name)

        return super(TitleFilterBackend, self).filter_queryset(request, queryset, view)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    filter_backends = [TitleFilterBackend]
    filter_fields = ['name', 'genre', 'category', 'year']
    permission_classes = [IsAdminOrReadOnlyPermission]
