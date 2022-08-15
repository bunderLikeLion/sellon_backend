from django.contrib import admin
from product.models import Product
from config.admin import linkify


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = (
        'id',
        'name',
        linkify(field_name='user'),
        'quality',
        'quantity',
        linkify(field_name='product_category'),
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
