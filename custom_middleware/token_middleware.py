from django.http import HttpResponseForbidden

from apps.main.auth_tokens.models import CustomToken


class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
            -1] if 'HTTP_AUTHORIZATION' in request.META else None

        if token:
            if is_token_valid(token):
                return self.get_response(request)
            else:
                return HttpResponseForbidden('Invalid token')
        else:
            return self.get_response(request)


def is_token_valid(token):
    try:
        exam_token = CustomToken.objects.get(key=token)
        return exam_token.is_valid()
    except CustomToken.DoesNotExist:
        return False
