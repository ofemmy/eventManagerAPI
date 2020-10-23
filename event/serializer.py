from rest_framework import serializers

from event.models import Event, EventRegistration
from users.serializer import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventRegistrationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = EventRegistration
        fields = ["id", "event", "user"]
