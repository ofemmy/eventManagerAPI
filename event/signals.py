from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from event.models import EventRegistration


@receiver(post_save, sender=EventRegistration)
def increment_num_of_registered(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        event.num_of_registered = F('num_of_registered') + 1
        event.save()


@receiver(post_delete, sender=EventRegistration)
def decrement_num_of_registered(sender, instance, **kwargs):
    event = instance.event
    event.num_of_registered = F('num_of_registered') - 1
    event.save()
