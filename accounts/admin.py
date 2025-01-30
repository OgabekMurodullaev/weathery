from django.contrib import admin
from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "is_active"]

admin.site.register(CustomUser, CustomUserAdmin)
