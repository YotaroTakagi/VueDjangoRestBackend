from django.urls import path, re_path
from app import views
from rest_framework import routers
from .views import UserViewSet, BlogViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', BlogViewSet)

urlpatterns = [
    path("sample/", views.SampleAPIView.as_view(), name="sample"),
    # path("post-blog/", views.PostBlogAPIView.as_view(), name="post_blog"),
]