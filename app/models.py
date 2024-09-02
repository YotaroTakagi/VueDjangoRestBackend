from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUsers(AbstractUser):
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        swappable = "AUTH_USER_MODEL"
        db_table = "custom_users_table"

    def __str__(self):
        return self.username


class BlogContents(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_contents"
    )
    click_count = models.IntegerField(default=0)
    good_count = models.IntegerField(default=0)
    bad_count = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    tag = models.CharField(max_length=30)
    meta_title = models.CharField(max_length=50, default="")
    meta_description = models.CharField(max_length=150, default="")
    body = models.TextField()
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "blog_contents_table"

    def __str__(self):
        return self.title
