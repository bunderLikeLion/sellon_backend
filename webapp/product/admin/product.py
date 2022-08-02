from django.contrib import admin
from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = (
        'name',
        'user',
        'quality',
        'quantity',
        'product_category',
        'status',
    )
    list_filter = (
        'status',
        'quality',
    )
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = (
        'name',
    )
    ordering = (
        'created_at',
        'updated_at',
        'quality',
        'quantity',
    )
