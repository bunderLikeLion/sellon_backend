from django.contrib import admin
from dealing.models import DealingEvaluation


@admin.register(DealingEvaluation)
class DealingEvaluationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'rate',
        'created_at',
        'updated_at',
    )
