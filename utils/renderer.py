from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        if str(status_code).startswith("2"):
            data = {'status': 'success', 'data': data}
        else:
            data = {'status': 'error', 'message': data['detail']}
        return super(CustomJSONRenderer, self).render(data, accepted_media_type, renderer_context)
