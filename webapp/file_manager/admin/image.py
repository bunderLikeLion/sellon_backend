from django.contrib import admin
from ..models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Admin View for Image'''

    list_display = ('id',)
    readonly_fields = ('thumbnail_preview',)
    ordering = ('created_at', 'updated_at')

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True
