from rest_framework import routers
from django.urls import path, include
from .views import ProfileViewSet, ActivityViewSet, TeamViewSet, WorkoutViewSet, LeaderboardViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
