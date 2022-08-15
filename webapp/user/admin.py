from django.contrib import admin
from .models.user import User
from .models.profile import Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile)
