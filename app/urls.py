from django.urls import path, re_path, include
from app import views
from rest_framework import routers
from .views import BlogViewSet, LoginAPIView, PickupBlogViewSet


router = routers.DefaultRouter()

router.register(r"blogs", BlogViewSet, basename="all_blogs")
router.register(r"pickup-blogs", PickupBlogViewSet, basename="pickup_blogs")

urlpatterns = [
    path(r"", include(router.urls)),
    path("login/", views.LoginAPIView.as_view(), name="login"),
]
