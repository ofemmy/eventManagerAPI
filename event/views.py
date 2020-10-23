# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from event.models import Event, EventRegistration
from event.permissions import IsEventOwnerOrReadOnly
from event.serializer import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, IsEventOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    def perform_update(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated, IsEventOwnerOrReadOnly]
