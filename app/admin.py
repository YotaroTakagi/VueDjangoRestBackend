from django.contrib import admin

from .models import User, Blog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    pass