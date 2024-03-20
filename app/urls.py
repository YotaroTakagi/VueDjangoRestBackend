from django.urls import path, re_path
from app import views

urlpatterns = [
    path("sample/", views.SampleAPIView.as_view(), name="sample"),
    # path("post-blog/", views.PostBlogAPIView.as_view(), name="post_blog"),
]