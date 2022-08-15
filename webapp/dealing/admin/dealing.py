from django.contrib import admin
from dealing.models import Dealing
from config.admin import linkify


def restart(self, request, queryset):
    for dealing in queryset:
        dealing.restart()


@admin.register(Dealing)
class DealingAdmin(admin.ModelAdmin):
    actions = [restart]

    list_display = (
        'id',
        linkify(field_name='product'),
        linkify(field_name='product_group'),
        'completed_at',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'completed_at',
    )
