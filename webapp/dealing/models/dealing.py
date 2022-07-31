from django.db import models
from config.models import SoftDeleteModel
from product.models.product import Product
from product.models.product_group import ProductGroup


class Dealing(SoftDeleteModel):

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
    created_at = models.DateTimeField(
        verbose_name='거래 생성 일시',
        null=True,
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='거래 수정 일시',
        null=True,
        blank=True,
        auto_now=True,
    )
    completed_at = models.DateTimeField(
        verbose_name='거래 완료 일시',
        null=True,
        blank=True,
    )
    deleted_at = models.DateTimeField(
        verbose_name='거래 삭제 일시',
        null=True,
        blank=True,
    )
