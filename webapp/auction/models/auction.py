from django.utils.timezone import now

from config import models
from config.models import SoftDeleteModel
from product.models import Product
from user.models import User


class Auction(SoftDeleteModel):

    class Meta:
        db_table = 'auctions'
        verbose_name = 'Auction'
        verbose_name_plural = 'Auctions'

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=False,
        verbose_name='유저',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
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
