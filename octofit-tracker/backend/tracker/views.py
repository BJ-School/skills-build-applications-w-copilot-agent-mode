from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from .models import Profile, Activity, Team, Workout, Leaderboard
from .serializers import UserSerializer, ProfileSerializer, ActivitySerializer, TeamSerializer, WorkoutSerializer, LeaderboardSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related("user").all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("members").all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related("user", "workout").all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.select_related("team", "user").all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.AllowAny]
