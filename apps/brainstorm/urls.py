from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BrainstormViewSet

router = DefaultRouter()
router.register("brainstorms",BrainstormViewSet,basename="brainstorms")


urlpatterns=[
    path('',include(router.urls)),
]