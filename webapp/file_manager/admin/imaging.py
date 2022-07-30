from django.contrib import admin
from ..models import Imaging


@admin.register(Imaging)
class ImagingAdmin(admin.ModelAdmin):
    '''Admin View for Imaging'''

    ordering = ('created_at', 'updated_at')
