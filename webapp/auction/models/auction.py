from django.db import transaction
from django.utils.timezone import now
from django.core.exceptions import ValidationError

from django.db import models
from config.models import BaseModel
from product.models import Product
from user.models import User


class Auction(BaseModel):
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
    title = models.CharField(
        verbose_name='경매 제목',
        null=False,
        blank=True,
        max_length=200,
        default='',
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
        blank=True,
    )
    dealing_type = models.IntegerField(
        verbose_name='거래 방법',
        null=False,
        choices=DEALING_TYPES,
        default=DIRECT_DEAL_TYPE,
        db_index=True,
    )
    product_groups_count = models.IntegerField(
        verbose_name='참여자 수',
        null=True,
        default=0,
    )

    def clean(self):
        previous_object = self.__class__.objects.filter(id=self.id).first()

        self.validate_product(previous_object)
        self.validate_owner(previous_object)

    def validate_product(self, previous_object):
        product = self.product
        if isinstance(product, int):
            product = Product.objects.find(pk=self.product)

        if previous_object is not None:

            if previous_object.product == product:

                return
            else:
                raise ValidationError({'product': '경매장에 등록한 물품은 변경할 수 없습니다.'})

        if product.status == Product.IN_AUCTION_STATUS:
            raise ValidationError({'product': '이미 경매장에 등록한 상품입니다.'})

        if product.status == Product.DEALING_STATUS:
            raise ValidationError({'product': '거래 진행중인 상품입니다.'})

        if product.status == Product.DEALED_STATUS:
            raise ValidationError({'product': '거래 완료한 상품입니다.'})

    def validate_owner(self, previous_object):
        if previous_object is not None and previous_object.owner != self.owner:
            raise ValidationError({'owner': '경매장을 연 사람은 변경할 수 없습니다.'})

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        self.product.status = Product.IN_AUCTION_STATUS
        self.product.save()
        super().save(force_insert, force_update, using, update_fields)

    @transaction.atomic
    def delete(self, using=None, keep_parents=False):
        self.product.status = Product.HIDDEN_STATUS
        self.product.save()

        super().delete(using, keep_parents)
