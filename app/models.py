from django.db import models

# Create your models here.
import uuid


class PostBlogContentModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', null=False, max_length=20, default='タイトル', help_text='最大20文字')
    tag = models.CharField(verbose_name='タグ', null=False,default='その他', max_length=20, help_text='最大20文字')
    html_content = models.TextField(verbose_name='本文', help_text='html形式で記載')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    