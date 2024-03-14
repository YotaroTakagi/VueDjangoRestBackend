from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.db import models
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
from .models import PostBlogContentModel

# admin.site.register(MyModel, MarkdownxModelAdmin)

"""
class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }


admin.site.register(MyModel, MyModelAdmin)
"""


# adminサイトに登録
admin.site.register(PostBlogContentModel, MarkdownxModelAdmin)