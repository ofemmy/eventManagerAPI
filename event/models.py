from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from users.models import User
from utils.models import Address


# Create your models here.
class Event(Address, models.Model):
    class EventCategory(models.TextChoices):
        BUSINESS_OR_PROFESSIONAL = 'Business/Professional'
        CHARITY_OR_CAUSES = 'Charity/Causes'
        COMMUNITY_OR_CULTURE = 'Community/Culture'
        EDUCATION = 'Education'
        FASHION_AND_BEAUTY = 'Fashion/Beauty'
        ENTERTAINMENT_MEDIA_FILM = 'Entertainment/Media'
        GOVERNMENT_OR_POLITICS = 'Government/Politics'
        HEALTH_AND_WELLNESS = 'Health/Wellness'
        LIFESTYLE = 'Lifestyle'
        MUSIC = 'Music'
        RELIGION_OR_SPIRITUALITY = 'Religion/Spirituality'
        SCIENCE_AND_TECH = 'Science/Tech'
        SPORT_AND_FITNESS = 'Sport/Fitness'
        TRAVEL_OR_OUTDOOR = 'Travel/Outdoor'
        PARTY = 'Party'
        OTHER = 'Other'

    class EventStatus(models.TextChoices):
        PUBLISHED = 'Published'
        PAST = 'Past'
        DRAFT = 'Draft'

    title = models.CharField(max_length=255)
    organizer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=30, choices=EventCategory.choices)
    status = models.CharField(max_length=10, choices=EventStatus.choices, default=EventStatus.DRAFT)
    max_attendees = models.IntegerField()
    num_of_registered = models.IntegerField()

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    registration_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'user',)

    def save(self, *args, **kwargs):
        event = self.event
        if event.num_of_registered == event.max_attendees:
            raise ValidationError(message="Maximum number of allowable attendees reached")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.event} - {self.user}"
