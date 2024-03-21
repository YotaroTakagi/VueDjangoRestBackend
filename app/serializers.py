# coding: utf-8

from rest_framework import serializers

from .models import User, Blog


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'tag', 'body', 'created_at', 'status', 'author')
