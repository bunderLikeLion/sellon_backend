from django.db import models, transaction
from django.forms import ValidationError
from config.models import BaseModel
from django.utils.timezone import now

from auction.models import Auction
from product.models.product import Product
from product.models.product_group import ProductGroup


class Dealing(BaseModel):

    class Meta:
        db_table = 'dealings'
        verbose_name = 'Dealing'
        verbose_name_plural = 'Dealings'

    auction = models.OneToOneField(
        Auction,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='경매장',
        related_name='dealing',
    )
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='물품',
        related_name='dealing',
    )
    product_group = models.OneToOneField(
        ProductGroup,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='물품 그룹',
        related_name='dealing',
    )
    completed_at = models.DateTimeField(
        verbose_name='거래 완료 일시',
        null=True,
        blank=True,
    )

    @property
    def in_progress(self):
        return self.completed_at is None

    @property
    def is_completed(self):
        return not self.in_progress

    @property
    def auction_obj(self):
        if isinstance(self.auction, int):
            return Auction.objects.find(pk=self.auction)
        return self.auction

    @property
    def product_obj(self):
        if isinstance(self.product, int):
            return Product.objects.find(pk=self.product)
        return self.product

    @property
    def product_group_obj(self):
        if isinstance(self.product_group, int):
            return ProductGroup.objects.find(pk=self.product_group)

        return self.product_group

    @transaction.atomic
    def complete(self):
        self.completed_at = now()
        self.save()

        self.product_obj.status = Product.DEALED_STATUS
        self.product_obj.user.completed_dealings_count += 1
        self.product_obj.save()
        self.product_obj.user.save()

        self.product_group_obj.user.completed_dealings_count += 1
        self.product_group_obj.user.save()
        self.product_group_obj.products.update(status=Product.DEALED_STATUS)

    @transaction.atomic
    def restart(self):
        self.completed_at = None
        self.save()

        self.product_obj.status = Product.DEALING_STATUS
        self.product_obj.save()

        self.product_group_obj.products.update(status=Product.DEALING_STATUS)

    def clean(self):
        if self.auction_obj.product != self.product_obj or self.auction_obj != self.product_group_obj.auction:
            raise ValidationError({'auction': '만들 수 없는 거래 정보입니다.'})

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        previous_object = self.__class__.objects.filter(id=self.id).first()

        if previous_object is None:
            # NOTE: 거래가 생성될 때
            self.auction_obj.end(by_dealing=True, dealing_product_group=self.product_group_obj)

        super().save(force_insert, force_update, using, update_fields)
