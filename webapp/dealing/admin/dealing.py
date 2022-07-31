from django.contrib import admin
from dealing.models import Dealing


@admin.register(Dealing)
class DealingAdmin(admin.ModelAdmin):
    pass
