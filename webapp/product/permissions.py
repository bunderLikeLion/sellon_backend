from django.db.models import Q
from rest_framework import permissions
from .models import ProductGroup, ProductGroupItem
from django.utils import timezone


class IsProductEditableOrDestroyable(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and (request.user == obj.user or request.user.is_staff)


# TODO: 나중에 바꿔주세요
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
        return request.user and obj.auction and not self.already_has_product_group_in_same_auction(request, obj) and not self.already_using_product_in_other_auction(request, obj)

    def editable(self, request, obj):
        return self.has_editable_permission(request, obj) and not self.already_using_product_in_other_auction(request, obj)

    def destroyable(self, request, obj):
        return self.has_editable_permission(request, obj) and timezone.now() < obj.auction.end_at

    def has_editable_permission(self, request, obj):
        return request.user and (request.user == obj.user or request.user.is_staff)

    def already_using_product_in_other_auction(self, request, obj):
        product_ids = request.data.get('product_ids') or []

        return ProductGroupItem.objects.filter(
            ~Q(product_group__auction=obj.auction_id) & Q(product__id__contains=product_ids)
        ).exists()

    def already_has_product_group_in_same_auction(self, request, obj):
        return ProductGroup.objects.filter(auction=obj.auction, user=request.user).exists()
