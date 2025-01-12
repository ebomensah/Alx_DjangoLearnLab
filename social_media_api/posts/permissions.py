from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    Assumes the model has a 'user' field that relates to the owner.
    """
    def has_object_permission(self, request, view, obj):
        # Allow read-only access to anyone
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow edit/delete only if the user is the owner of the object
        return obj.author == request.user
