# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from event.models import Event, EventRegistration
from event.permissions import IsEventOwnerOrReadOnly, IsEventRegistrationOwnerOrReadOnly
from event.serializer import EventSerializer, EventRegistrationSerializer
from users.models import User


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
    permission_classes = [IsAuthenticated, IsEventRegistrationOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        event_id = request.data['event_id']
        try:
            already_existing_event_reg = EventRegistration.objects.filter(event__id=event_id, user__id=user_id)
            if len(already_existing_event_reg) > 0:
                return Response({'detail': 'Event Registration exists already'}, status=status.HTTP_400_BAD_REQUEST)
            new_event_reg = EventRegistration.objects.create(event=Event.objects.get(pk=event_id),
                                                             user=User.objects.get(pk=user_id))
            serializer = EventRegistrationSerializer(new_event_reg)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist or Event.DoesNotExist:
            return Response({'detail': 'User or Event not found'}, status.HTTP_404_NOT_FOUND)


test = {"user_id": 8, "event_id": 1}
