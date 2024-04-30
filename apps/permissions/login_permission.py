from rest_framework.permissions import BasePermission


class LogInUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'POST'
