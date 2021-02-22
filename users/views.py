import uuid

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, \
    permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from api_yamdb import settings
from .models import User
from .permissions import AdminPermission
from .serializers import UserSerializer, EmailSerializer, TokenSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def confirmation_code_sender(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = serializer.data['email']
    user_is_exist = User.objects.filter(email=email).exists()
    if not user_is_exist:
        User.objects.create_user(username=email, email=email)

    confirmation_code = uuid.uuid3(uuid.NAMESPACE_DNS, email)

    send_mail(
        subject='Ваш персональный код от сервиса YamDb',
        from_email=settings.DEFAULT_FROM_EMAIL,
        message=f'Ваш код: {confirmation_code}, он будет действовать 24 часа.',
        recipient_list=[email],
        fail_silently=False,
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminPermission]
    lookup_field = 'username'


class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = User.objects.get(username=request.user.username)
        serializer = UserSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
