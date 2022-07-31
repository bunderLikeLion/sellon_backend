from django.db import models
from config.models import SoftDeleteModel
from product.models import Product
from .product_group import ProductGroup


class ProductGroupItem(SoftDeleteModel):

    class Meta:
        db_table = 'product_group_items'
        verbose_name = 'ProductGroupItem'
        verbose_name_plural = 'ProductGroupItems'

    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.CASCADE,
        verbose_name='물품 그룹'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='물품'
    )
