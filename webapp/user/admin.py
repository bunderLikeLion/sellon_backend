from django.contrib import admin
from django.core.files import File

from .models.user import User, get_random_profile_filename


def reset_avatar(self, request, querset):
    for user in querset:
        filename = get_random_profile_filename()
        f = open('static/' + filename, 'rb')
        user.avatar = File(f)
        user.save()
        f.close()


def reset_counters(self, request, queryset):
    for user in queryset:
        user.completed_dealings_count = 0
        user.save()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    actions = [reset_avatar, reset_counters]

    list_per_page = 10
    list_display = [
        'id',
        'email',
        'username',
        'avatar_preview',
    ]
    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        return obj.avatar_preview

    avatar_preview.short_description = 'Thumbnail Preview'
    avatar_preview.allow_tags = True
