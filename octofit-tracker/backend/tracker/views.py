from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from .models import Profile, Activity
from .serializers import UserSerializer, ProfileSerializer, ActivitySerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related("user").all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related("user").all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
