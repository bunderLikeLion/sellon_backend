from django.db import models
from config.models import BaseModel
from product.models.product_category import ProductCategory


class Product(BaseModel):

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    QUALITY_CHOICES = (
        (1, '하'),
        (2, '중하'),
        (3, '중'),
        (4, '중상'),
        (5, '상'),
    )

    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='물품 카테고리'
    )
    user = models.ForeignKey(
        'user.User',
        null=True,
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
        on_delete=models.SET_NULL,
        verbose_name='썸네일',
    )
