from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

router_v1 = DefaultRouter()
router_v1.register('', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/categories/', include(router_v1.urls)),
]