from auction.models import InterestedAuction
from django.contrib import admin


@admin.register(InterestedAuction)
class InterestedAuctionAdmin(admin.ModelAdmin):
    '''Admin View for Auction'''

    list_display = (
        'id',
        'user',
        'auction'
    )
    list_filter = (
        'user_id',
    )
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = ()
    ordering = (
        'created_at',
        'updated_at',
    )
