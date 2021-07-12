from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CubingViewSet

router = DefaultRouter()
router.register("cubing",CubingViewSet,basename="cubing")


urlpatterns=[
    path('',include(router.urls)),
]