from product.models import ProductGroup
from django.contrib import admin


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    pass
