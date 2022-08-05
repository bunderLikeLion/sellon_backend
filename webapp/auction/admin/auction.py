from auction.models import Auction
from django.contrib import admin


def delete_queryset(self, request, queryset):
    for obj in queryset:
        obj.delete()


@admin.register(Auction)
class AuctionAdmin(admin.ModelAdmin):
    '''Admin View for Auction'''
    actions = [delete_queryset]

    list_display = (
        'id',
        'title',
        'product',
        'description',
        'start_at',
        'end_at',
        'product_groups_count',
    )
    list_filter = (
        'start_at',
        'end_at',
    )
    raw_id_fields = ()
    readonly_fields = ('product_groups_count',)
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
