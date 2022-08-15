from django.db import models

from config.models import BaseModel


class ProductImage(BaseModel):
    class Meta:
        db_table = 'product_images'
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'

    image = models.ForeignKey(
        'file_manager.Image',
        related_name='product_image_items',
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'product.Product',
        related_name='product_image_items',
        on_delete=models.CASCADE,
    )
