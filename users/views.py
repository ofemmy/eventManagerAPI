# Create your views here.
from django.contrib.auth.models import AnonymousUser
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.models import User, UserProfile
from users.permissions import IsUserOrReadOnly, IsAuthenticatedWithCreateExemption, IsProfileOwnerOrReadOnly
from users.serializer import UserSerializer, UserProfileSerializer


@api_view(["GET"])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'profiles': reverse('user-profile-list', request=request, format=format),
        'events': reverse('event-list', request=request, format=format)
    })


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

    def get_object(self):
        """
        This function makes sure that it is the user id
        that is used to query the profile and not just the
        profile id
        """
        queryset = self.get_queryset()
        filter = {'user__id': self.kwargs["pk"]}
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
