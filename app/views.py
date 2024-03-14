from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.serializers import UserSerializer, GroupSerializer
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import PostBlogContentModel
from .serializers import BlogContentSerializer

import cv2


class SampleAPIView(APIView):
    def get(self, request):
        print('sample')
        
        return Response('Sample TEST OK', status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BlogContentSerializer(data=request.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostBlogAPIView(APIView):
    def get(self, request):
        queryset = PostBlogContentModel.objects.all()


        return Response(queryset, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]





