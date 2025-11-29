from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


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

    def __str__(self):
        return f"{self.user.username} {self.activity_type} {self.date.date()}"
