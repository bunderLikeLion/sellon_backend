from django.db import transaction
from django.db import models
from django.utils import timezone

from config.models import BaseModel
from product.models import Product
from .product_group import ProductGroup


class ProductGroupItem(BaseModel):

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

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.product_group and self.product_group.auction and self.product_group.auction.end_at and self.product_group.auction.end_at <= timezone.now():
            self.product.status = Product.IN_AUCTION_STATUS
        else:
            self.product.status = Product.HIDDEN_STATUS
        self.product.save()
        super().save(force_insert, force_update, using, update_fields)

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.product.status = Product.HIDDEN_STATUS
        self.product.save()

        super().delete(using, keep_parents)
