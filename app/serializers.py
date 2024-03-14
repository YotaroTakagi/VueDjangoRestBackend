from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PostBlogContentModel
import markdown


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BlogContentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = PostBlogContentModel
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
    