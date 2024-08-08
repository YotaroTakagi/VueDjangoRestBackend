# coding: utf-8

from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import CustomUsers, BlogContents


class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = "__all__"


class BlogContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContents
        fields = "__all__"
