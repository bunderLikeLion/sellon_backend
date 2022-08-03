from django.contrib import admin
from ..models import ProductImage


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    '''Admin View for Imaging'''

    ordering = ('created_at', 'updated_at')
