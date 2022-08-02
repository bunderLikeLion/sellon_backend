from rest_framework import permissions


class IsProductEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user == obj.user or request.user.is_staff)


class IsProductGroupEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'POST':
            return self.creatable(request, obj)

        if request.method == 'DELETE':
            return self.destroyable(request, obj)

        return self.editable(request, obj)

    def creatable(self, request, obj):
        return request.user and obj.auction

    def editable(self, request, obj):
        return self.has_editable_permission(request, obj)

    def destroyable(self, request, obj):
        return self.has_editable_permission(request, obj)

    def has_editable_permission(self, request, obj):
        return request.user and (request.user == obj.user or request.user.is_staff)
