# RestFramework
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed

# Project
from apps.main.auth_tokens.models import CustomToken


class IsCustomTokenAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
            1] if 'HTTP_AUTHORIZATION' in request.META else None

        if not token:
            raise AuthenticationFailed('No token provided.')

        try:
            custom_token = CustomToken.objects.get(key=token)
            if custom_token:
                return True
            else:
                raise AuthenticationFailed('Invalid token.')
        except CustomToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')


class IsTeacherTokenAuthenticatedPermission(BasePermission):
    def has_permission(self, request, view):
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[
            1] if 'HTTP_AUTHORIZATION' in request.META else None

        if not token:
            raise AuthenticationFailed('No token provided.')

        try:
            custom_token = CustomToken.objects.get(key=token, is_student=False)
            if custom_token:
                return True
            else:
                raise AuthenticationFailed('Invalid token.')
        except CustomToken.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')
