# Generated by Django 5.0.3 on 2024-03-23 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="blog", name="author",),
    ]
