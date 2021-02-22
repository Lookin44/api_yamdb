from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import User
from .permissions import AdminPermission
from .serializers import UserSerializer


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

