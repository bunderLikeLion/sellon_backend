from django.db import models
from config.models import BaseModel


class Product(BaseModel):

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    HIDDEN_STATUS = 0
    IN_AUCTION_STATUS = 1
    DEALING_STATUS = 2
    DEALED_STATUS = 3

    QUALITY_CHOICES = (
        (1, 'very_poor'),
        (2, 'poor'),
        (3, 'good'),
        (4, 'very_good'),
        (5, 'excellent'),
    )

    STATUS_CHOICES = (
        (HIDDEN_STATUS, 'hidden'),
        (IN_AUCTION_STATUS, 'in_auction'),
        (DEALING_STATUS, 'dealing'),
        (DEALED_STATUS, 'dealed'),
    )

    product_category = models.ForeignKey(
        'ProductCategory',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='물품 카테고리'
    )
    user = models.ForeignKey(
        'user.User',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='유저'
    )
    name = models.CharField(
        verbose_name='물품 명',
        null=False,
        blank=False,
        max_length=100,
    )
    description = models.TextField(
        verbose_name='물품 설명',
        null=True,
        blank=True,
        max_length=300,
    )
    quantity = models.IntegerField(
        verbose_name='수량',
        null=False,
        default=1,
    )
    quality = models.IntegerField(
        verbose_name='품질',
        null=False,
        choices=QUALITY_CHOICES,
        default=3,
        db_index=True,
    )
    status = models.IntegerField(
        verbose_name='상태',
        null=False,
        choices=STATUS_CHOICES,
        default=0,
        db_index=True,
    )
    abstract = models.CharField(
        verbose_name='요약',
        null=True,
        blank=True,
        max_length=100,
    )
    thumbnail = models.ForeignKey(
        'file_manager.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name='썸네일',
    )
    images = models.ManyToManyField(
        'file_manager.Image',
        through='file_manager.ProductImage',
        related_name='product_images',
    )
    dealing_at = models.DateTimeField(
        verbose_name='거래 시작 일시',
        null=True,
        blank=True,
    )
    dealed_at = models.DateTimeField(
        verbose_name='거래 완료 일시',
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f'[{self.id}] {self.name}'
