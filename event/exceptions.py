import logging

from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler

LOG = logging.getLogger(__name__)


def custom_exception_handler(exception, context):
    global detail
    if isinstance(exception, DjangoValidationError):
        if hasattr(exception, 'message_dict'):
            detail = exception.message_dict
        elif hasattr(exception, 'message'):
            detail = exception.message
        elif hasattr(exception, 'messages'):
            detail = exception.messages
        else:
            LOG.error("BAD VALIDATION MESSAGE: %s", exception)
        exception = DRFValidationError(detail=detail)
    return drf_exception_handler(exception, context)
