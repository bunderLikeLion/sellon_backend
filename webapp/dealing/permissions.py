from rest_framework import permissions


class OnlyAuctionOwnerCreateDealingPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.method != 'POST':
            # NOTE: 거래는 유저가 삭제/수정할 수 없습니다.
            return False

        return request.user
