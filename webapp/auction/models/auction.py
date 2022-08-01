from django.utils.timezone import now

from django.db import models
from config.models import SoftDeleteModel
from product.models import Product
from user.models import User


class Auction(SoftDeleteModel):

    class Meta:
        db_table = 'auctions'
        verbose_name = 'Auction'
        verbose_name_plural = 'Auctions'

    DIRECT_DEAL_TYPE = 0
    DELIVERY_DEAL_TYPE = 1

    DEALING_TYPES = (
        (DIRECT_DEAL_TYPE, 'direct'),
        (DELIVERY_DEAL_TYPE, 'delivery'),
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='유저',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='물품',
    )
    description = models.CharField(
        verbose_name='경매 설명',
        null=False,
        blank=True,
        max_length=200,
    )
    start_at = models.DateTimeField(
        verbose_name='경매 시작 일시',
        null=True,
        default=now,
    )
    end_at = models.DateTimeField(
        verbose_name='경매 종료 일시',
        null=True,
    )
    dealing_type = models.IntegerField(
        verbose_name='거래 방법',
        null=False,
        choices=DEALING_TYPES,
        default=DIRECT_DEAL_TYPE,
        db_index=True,
    )
