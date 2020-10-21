# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

from users.models import User, UserProfile
from users.permissions import IsUserOrReadOnly, IsAuthenticatedWithCreateExemption, IsProfileOwnerOrReadOnly
from users.serializer import UserSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedWithCreateExemption, IsUserOrReadOnly]

    def list(self, request, *args, **kwargs):
        """
        only logged in users and admin users can get full list of users
        """
        if isinstance(request.user, AnonymousUser) or not request.user.is_admin:
            raise PermissionDenied(code=403, detail="You have to be logged in admin user to access this resource")
        return super().list(request, *args, **kwargs)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        """
        only logged in admin users can get full list of profiles
        """
        if isinstance(request.user, AnonymousUser) or not request.user.is_admin:
            raise PermissionDenied(code=403, detail="You have to be logged in admin user to access this resource")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
