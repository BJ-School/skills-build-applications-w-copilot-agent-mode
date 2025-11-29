from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Activity, Team, Workout, Leaderboard


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "user", "display_name", "bio"]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "name", "description", "duration_minutes", "difficulty"]


class TeamSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "description", "members", "created_at"]


class ActivitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    workout = WorkoutSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "date", "notes", "workout"]


class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ["id", "team", "user", "total_minutes", "total_distance", "rank"]
    user = UserSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ["id", "user", "activity_type", "duration_minutes", "distance_km", "date", "notes"]
