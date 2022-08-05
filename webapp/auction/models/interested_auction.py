from auction.models import Auction
from config.models import BaseModel
from django.db import models
from user.models import User


class InterestedAuction(BaseModel):
    class Meta:
        db_table = 'interested_auctions'
        verbose_name = 'InterestedAuction'
        verbose_name_plural = 'InterestedAuctions'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'auction'],
                name='unique_interested_auction_by_user',
            )
        ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='유저',
    )
    auction = models.ForeignKey(
        Auction,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='경매장',
    )
