from product.models import ProductGroup
from django.contrib import admin


def delete_queryset(self, request, queryset):
    for obj in queryset:
        obj.delete()


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    actions = [delete_queryset]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
