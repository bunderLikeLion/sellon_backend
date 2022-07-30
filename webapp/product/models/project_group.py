from auction.models.auction import Auction
from django.db import models
from config.models import SoftDeleteModel
from user.models import User


class ProductGroup(SoftDeleteModel):

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
