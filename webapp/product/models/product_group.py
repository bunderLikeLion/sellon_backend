from django.db import models
from django.db import transaction
from django.forms import ValidationError

from auction.models.auction import Auction
from config.models import BaseModel
from user.models import User
from .product import Product


class ProductGroup(BaseModel):

    class Meta:
        db_table = 'product_groups'
        verbose_name = 'ProductGroup'
        verbose_name_plural = 'ProductGroups'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'auction'],
                name='unique_product_group_in_auction_by_user',
            )
        ]

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

    @property
    def auction_obj(self):
        return Auction.objects.find(pk=self.auction) if isinstance(self.auction, int) else self.auction

    def validate_already_ended_acution(self):
        if self.auction_obj.is_ended:
            raise ValidationError({'auction': '종료된 경매장에 등록한 상품 목록은 수정할 수 없습니다'})

    def validate_self_participating(self):
        if self.auction_obj.owner == self.user:
            raise ValidationError({'auction': '자신이 만든 경매장에는 참여할 수 없습니다'})

    def validate_editing_auction(self, previous_object):
        if self.auction_obj.id != previous_object.auction.id:
            raise ValidationError({'auction': '경매장 정보는 수정할 수 없습니다.'})

    def clean(self):
        previous_object = self.__class__.objects.filter(id=self.id).first()

        self.validate_editing_auction(previous_object)
        self.validate_self_participating()
        self.validate_already_ended_acution()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.validate_already_ended_acution()

        self.products.update(status=Product.HIDDEN_STATUS)
        super().delete(using, keep_parents)
