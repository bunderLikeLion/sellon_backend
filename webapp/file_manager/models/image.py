from django.db import models
from config.models import BaseModel
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail


class Image(BaseModel):
    class Meta:
        db_table = 'images'
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    file = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )
    uploader = models.ForeignKey(
        'user.User',
        related_name='uploader',
        on_delete=models.SET_NULL,
        null=True
    )

    @property
    def thumbnail_preview(self):
        if self.file:
            _thumbnail = get_thumbnail(self.file,
                                       '300x300',
                                       upscale=False,
                                       crop=False,
                                       quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(
                _thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ''
