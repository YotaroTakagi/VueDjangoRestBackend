from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUsers, BlogContents


@admin.register(CustomUsers)
class CustomUsersAdmin(UserAdmin):
    model = CustomUsers
    # 必要なフィールドのみ表示
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    list_display = ("username", "is_staff", "is_active")
    search_fields = ("username",)
    ordering = ("username",)


@admin.register(BlogContents)
class BlogContentsAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "created_at", "updated_at")
    search_fields = ("title", "tag", "body")
    list_filter = ("status", "tag", "created_at")
    ordering = ("created_at",)
