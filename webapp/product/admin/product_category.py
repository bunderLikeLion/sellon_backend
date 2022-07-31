from django.contrib import admin
from product.models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    '''Admin View for ProductCategory'''

    list_display = (
        'id',
        'name',
    )
    list_filter = ()
    raw_id_fields = ()
    readonly_fields = ()
    search_fields = (
        'name',
    )
    ordering = (
        'created_at',
        'updated_at',
    )
