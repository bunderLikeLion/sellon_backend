from django.utils import timezone
from rest_framework import permissions


class IsAuctionEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'DELETE' and getattr(obj, 'end_at') <= timezone.now():
            return False

        return request.user and (request.user == obj.owner or request.user.is_staff)


class IsInterestedAuctionEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user == obj.user)
