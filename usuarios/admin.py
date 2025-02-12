from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "phone_number", "user_type", "is_staff", "is_active"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone_number", "user_type")}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
