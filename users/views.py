# Create your views here.
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsUserOrReadOnly
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsUserOrReadOnly]

    def list(self, request, *args, **kwargs):
        if not request.user.is_admin:
            raise PermissionDenied(code=403, detail="You have to be admin user to access this resource")
        return super().list(request, *args, **kwargs)
