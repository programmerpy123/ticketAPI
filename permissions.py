from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrReadonly(BasePermission):
    message = "access denied, the user is not ower of question."

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user == obj.User