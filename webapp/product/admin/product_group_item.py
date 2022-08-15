from product.models import ProductGroupItem
from django.contrib import admin


def delete_queryset(self, request, queryset):
    for obj in queryset:
        obj.delete()


@admin.register(ProductGroupItem)
class ProductGroupItemAdmin(admin.ModelAdmin):
    actions = [delete_queryset]

    list_display = [
        'id',
        'product_group',
        'product',
        'created_at',
        'updated_at',
    ]
    list_filter = (
        'product_group',
        'product',
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
