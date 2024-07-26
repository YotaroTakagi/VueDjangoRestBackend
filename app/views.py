from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from .models import BlogContents
from .serializers import BlogContentsSerializer


class SampleAPIView(APIView):
    def get(self, request):

        return Response("Hello Django!!!")


class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogContents.objects.all()
    serializer_class = BlogContentsSerializer
