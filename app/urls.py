from django.urls import path, re_path
from app import views
from rest_framework import routers
from .views import BlogViewSet


router = routers.DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path("sample/", views.SampleAPIView.as_view(), name="sample"),
]