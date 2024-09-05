from django.urls import path, re_path, include
from app import views
from rest_framework import routers
from .views import AllBlogViewSet, LoginAPIView, PickupBlogViewSet, LatestBlogViewSet


router = routers.DefaultRouter()

router.register(r"all-blogs", AllBlogViewSet, basename="all_blogs")
router.register(r"latest-blogs", LatestBlogViewSet, basename="latest_blogs")
router.register(r"pickup-blogs", PickupBlogViewSet, basename="pickup_blog")

urlpatterns = [
    path(r"", include(router.urls)),
    path("login/", views.LoginAPIView.as_view(), name="login"),
]
