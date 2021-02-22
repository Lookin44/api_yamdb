from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserInfo, confirmation_code_sender, get_token

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/email/', confirmation_code_sender),
    path('v1/auth/token/', get_token),
    path('v1/users/me/', UserInfo.as_view()),
    path('v1/', include(router_v1.urls)),
]
