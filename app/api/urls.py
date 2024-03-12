from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewsets import F1ResultView

router = DefaultRouter()
router.register(prefix="f1", viewset=F1ResultView)


urlpatterns = [
    path("api/", include(router.urls))
]
