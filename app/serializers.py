# coding: utf-8

from rest_framework import serializers
from .models import CustomUsers, BlogContents


class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = "__all__"


class BlogContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContents
        fields = "__all__"
