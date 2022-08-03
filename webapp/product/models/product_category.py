from django.db import models

from config.models import BaseModel


class ProductCategory(BaseModel):

    class Meta:
        db_table = 'product_categories'
        verbose_name = 'ProductCategory'
        verbose_name_plural = 'ProductCategories'

    name = models.CharField(
        verbose_name='카테고리 명',
        null=False,
        blank=False,
        max_length=100,
    )
    primary = models.BooleanField(
        verbose_name='주요 분류 유무',
        null=False,
        blank=False,
        default=False,
    )
    display_order = models.IntegerField(
        verbose_name='전시 순서',
        null=False,
        blank=False,
        default=0,
    )

    def __str__(self) -> str:
        return f'[{self.id}] {self.name}'
