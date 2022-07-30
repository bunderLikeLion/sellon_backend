from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from config.models import BaseModel


class Imaging(BaseModel):
    class Meta:
        db_table = 'imagings'
        verbose_name = 'Imaging'
        verbose_name_plural = 'Imagings'

    image = models.ForeignKey('Image', related_name='image', on_delete=models.CASCADE)
    imageable_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.SET_NULL,
        null=True,
    )
    imageable_id = models.PositiveIntegerField(
        null=True,
    )
    imageable = GenericForeignKey('imageable_type', 'imageable_id')
