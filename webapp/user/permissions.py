from rest_framework import permissions


class IsEvaluationEditable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user == obj.evaluator or request.user.is_staff)
