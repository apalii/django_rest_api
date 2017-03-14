from rest_framework import permissions
from rest_framework.compat import is_authenticated


class IsAdminOrReadOnlyForAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to authenticated users only,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return request.user and is_authenticated(request.user)

        # Allows access only to admin users for put/update/delete.
        return request.user and request.user.is_staff
