from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import InvertViewSet

router = DefaultRouter()
router.register("inverts",InvertViewSet,basename="inverts")


urlpatterns=[
    path('',include(router.urls)),
]