from event.views import EventViewSet, EventRegistrationViewSet

event_list = EventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
event_detail = EventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
event_registration_list = EventRegistrationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
event_registration_detail = EventRegistrationViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})
