# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from users.models import User
from users.permissions import IsUserOrReadOnly, IsAuthenticatedWithCreateExemption
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedWithCreateExemption, IsUserOrReadOnly]


    def list(self, request, *args, **kwargs):
        """
        only logged in users and admin users can get full list of users
        """
        if isinstance(request.user, AnonymousUser) or not request.user.is_admin:
            raise PermissionDenied(code=403, detail="You have to be logged in and admin user to access this resource")
        return super().list(request, *args, **kwargs)
