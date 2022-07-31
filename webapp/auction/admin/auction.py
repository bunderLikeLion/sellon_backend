from auction.models import Auction
from django.contrib import admin


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    '''Admin View for Auction'''

    list_display = (
        'description',
        'start_at',
        'end_at',
    )
    list_filter = (
        'start_at',
        'end_at',
    )
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = ()
    ordering = (
        'created_at',
        'updated_at',
        'start_at',
    )
