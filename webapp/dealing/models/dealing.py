from django.db import models
from config.models import BaseModel
from product.models.product import Product
from product.models.product_group import ProductGroup


class Dealing(BaseModel):

    class Meta:
        db_table = 'dealings'
        verbose_name = 'Dealing'
        verbose_name_plural = 'Dealings'

    STATUS_CHOICES = (
        (0, 'IN_PROGRESS'),
        (1, 'COMPLETED'),
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='물품'
    )
    product_group = models.ForeignKey(
        ProductGroup,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='물품 그룹'
    )
    status = models.IntegerField(
        verbose_name='상태',
        null=True,
        choices=STATUS_CHOICES,
        default=0,
        db_index=True,
    )
    completed_at = models.DateTimeField(
        verbose_name='거래 완료 일시',
        null=True,
        blank=True,
    )
