from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from .models import BlogContents
from .serializers import BlogContentsSerializer, CustomUsersSerializer


class SampleAPIView(APIView):
    def get(self, request):

        return Response("Hello Django!!!")


class AllBlogViewSet(viewsets.ModelViewSet):
    queryset = BlogContents.objects.all()
    serializer_class = BlogContentsSerializer


class LatestBlogViewSet(viewsets.ModelViewSet):
    queryset = BlogContents.objects.filter(status="public").order_by("-created_at")[:5]
    serializer_class = BlogContentsSerializer


class PickupBlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogContentsSerializer

    def retrieve(self, request, pk=None):
        # `get_object_or_404` を使用して、特定のIDのデータを素早く取得
        blog = get_object_or_404(BlogContents, id=pk)
        serializer = BlogContentsSerializer(blog)
        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        request_data = request.data

        if (
            request_data["user_name"] == "admin_x"
            and request_data["password"] == "admin_x"
        ):
            print("OK")
            return Response({"message": "Post successful"}, status=status.HTTP_200_OK)
        else:
            print("NG")
            return Response(
                {"message": "Post erro"}, status=status.HTTP_400_BAD_REQUEST
            )
