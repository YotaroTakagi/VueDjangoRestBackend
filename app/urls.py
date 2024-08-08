from django.urls import path, re_path, include
from app import views
from rest_framework import routers
from .views import BlogViewSet, LoginAPIView


router = routers.DefaultRouter()

router.register(r"blogs", BlogViewSet)

urlpatterns = [
    path(r"", include(router.urls)),
    path("login/", views.LoginAPIView.as_view(), name="login"),
]
