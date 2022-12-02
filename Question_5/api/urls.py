from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from api.views import UserCreateAPIView, ReadOnlyUserModelViewSet

router = DefaultRouter()

router.register('user', ReadOnlyUserModelViewSet)

urlpatterns = [
    path('user_create/', UserCreateAPIView.as_view()),
    path('', include(router.urls))
]
