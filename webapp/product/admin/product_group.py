from product.models import ProductGroup
from django.contrib import admin
from config.admin import linkify


def delete_queryset(self, request, queryset):
    for obj in queryset:
        obj.delete()


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    actions = [delete_queryset]

    list_display = [
        'id',
        linkify(field_name='user'),
        linkify(field_name='auction'),
        'created_at',
        'updated_at',
    ]
    list_filter = (
        'user',
        'auction',
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
