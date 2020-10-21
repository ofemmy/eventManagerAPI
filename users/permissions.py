from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class IsAuthenticatedWithCreateExemption(permissions.BasePermission):
    """
    only grant permission for creating new resource even without logging in
    For example I can create a new user without needing to log in
    """

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        else:
            return False
