from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import ImageViewSet

router = DefaultRouter()
router.register(r'images', ImageViewSet)

urlpatterns = [
    url('', include(router.urls))
]
