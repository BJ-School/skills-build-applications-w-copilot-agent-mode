from rest_framework import routers
from django.urls import path, include
from .views import ProfileViewSet, ActivityViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
