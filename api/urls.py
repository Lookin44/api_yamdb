from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet

router_v1 = DefaultRouter()
router_v1.register('', CategoryViewSet, basename='categories')
router_v1.register('', GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/categories/', include(router_v1.urls)),
    path('v1/genres/', include(router_v1.urls)),
]
