from django.apps import AppConfig


class EventConfig(AppConfig):
    name = 'event'

    # noinspection PyUnresolvedReferences
    def ready(self):
        import event.signals
