from django.contrib import admin
from ..models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Admin View for Image'''

    ordering = ('created_at', 'updated_at')
