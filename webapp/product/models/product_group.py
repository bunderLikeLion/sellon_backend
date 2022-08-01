from django.db import models
from django.db import transaction

from auction.models.auction import Auction
from config.models import BaseModel
from user.models import User
from .product import Product


class ProductGroup(BaseModel):

    class Meta:
        db_table = 'product_groups'
        verbose_name = 'ProductGroup'
        verbose_name_plural = 'ProductGroups'

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        verbose_name='경매'
    )
    money = models.IntegerField(
        verbose_name='추가 금액',
        null=True,
        default=0,
    )
    description = models.CharField(
        verbose_name='물품 그룹 설명',
        max_length=200,
        blank=True,
    )
    products = models.ManyToManyField(
        'product.Product',
        through='product.ProductGroupItem'
    )

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.products.update(status=Product.HIDDEN_STATUS)
        super().delete(using, keep_parents)
