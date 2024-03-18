from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path
from .viewsets import F1ResultView
from .. import views

router = DefaultRouter()
router.register(prefix="f1", viewset=F1ResultView)


urlpatterns = [
    path("api/", include(router.urls)),
    path('mostrar/', views.mostrar),
    path('form/', views.formulario, name='form')
    
]
