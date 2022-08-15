from auction.models import Auction
from django.contrib import admin
from config.admin import linkify
from auction.models import InterestedAuction
from product.models import ProductGroup


def delete_queryset(self, request, queryset):
    for obj in queryset:
        obj.delete()


def restart(self, request, queryset):
    for auction in queryset:
        auction.restart()


def reset_counters(self, request, queryset):
    for auction in queryset:
        auction.product_groups_count = ProductGroup.objects.filter(auction=auction).count()
        auction.interested_auctions_count = InterestedAuction.objects.filter(auction=auction).count()
        auction.save()


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    '''Admin View for Auction'''
    actions = [delete_queryset, restart, reset_counters]

    list_display = (
        'id',
        'title',
        linkify(field_name='product'),
        'description',
        'start_at',
        'end_at',
        'product_groups_count',
        'interested_auctions_count',
    )
    list_filter = (
        'start_at',
        'end_at',
    )
    raw_id_fields = ()
    readonly_fields = (
        'product_groups_count',
        'interested_auctions_count'
    )
    search_fields = (
        'title',
    )
    ordering = (
        'created_at',
        'updated_at',
        'start_at',
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
