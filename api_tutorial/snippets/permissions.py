from rest_framework import permissions


class IsOwnerorReadOnly(permissions.BasePermission):
    # custom permission
    def has_object_permission(self, request, view, obj):
        # read access to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
