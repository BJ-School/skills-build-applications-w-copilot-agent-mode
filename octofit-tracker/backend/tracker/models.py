from django.conf import settings
from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="teams")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField()
    difficulty = models.CharField(max_length=32, choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")], default="medium")

    def __str__(self):
        return self.name


class Activity(models.Model):
    ACTIVITY_CHOICES = [
        ("run", "Run"),
        ("bike", "Bike"),
        ("swim", "Swim"),
        ("walk", "Walk"),
        ("workout", "Workout"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.CharField(max_length=32, choices=ACTIVITY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    workout = models.ForeignKey(Workout, on_delete=models.SET_NULL, null=True, blank=True, related_name="activities")

    def __str__(self):
        return f"{self.user.username} {self.activity_type} {self.date.date()}"


class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="leaderboards")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="leaderboard_entries")
    total_minutes = models.PositiveIntegerField(default=0)
    total_distance = models.FloatField(default=0)
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.user.username} (Rank {self.rank})"
