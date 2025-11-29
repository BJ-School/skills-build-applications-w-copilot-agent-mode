from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Activity


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "display_name", "bio"]


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "date", "notes"]
