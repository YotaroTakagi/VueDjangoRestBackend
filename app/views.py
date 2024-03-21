from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .models import User, Blog
from .serializers import UserSerializer, BlogSerializer


class SampleAPIView(APIView):
    def get(self, request):
        
        return Response('Hello Django!!!')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
