from django.urls import path, re_path, include
from app import views
from rest_framework import routers
from .views import BlogViewSet


router = routers.DefaultRouter()
router.register(r"blogs", BlogViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
