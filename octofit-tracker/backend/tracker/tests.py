from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Workout, Activity, Leaderboard, Profile

class ModelSmokeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)
        self.workout = Workout.objects.create(name="Test Workout", duration_minutes=30, difficulty="easy")
        self.profile = Profile.objects.create(user=self.user, display_name="Test User")
        self.activity = Activity.objects.create(user=self.user, activity_type="run", duration_minutes=20, workout=self.workout)
        self.leaderboard = Leaderboard.objects.create(team=self.team, user=self.user, total_minutes=20, total_distance=5.0, rank=1)

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "testuser")

    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")

    def test_workout_str(self):
        self.assertEqual(str(self.workout), "Test Workout")

    def test_activity_str(self):
        self.assertIn("testuser", str(self.activity))

    def test_leaderboard_str(self):
        self.assertIn("Test Team", str(self.leaderboard))
        self.assertIn("testuser", str(self.leaderboard))

from rest_framework.test import APIClient
class APISmokeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="apiuser", password="apipass")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.team = Team.objects.create(name="API Team")
        self.team.members.add(self.user)
        self.workout = Workout.objects.create(name="API Workout", duration_minutes=45, difficulty="medium")
        self.profile = Profile.objects.create(user=self.user, display_name="API User")
        self.activity = Activity.objects.create(user=self.user, activity_type="bike", duration_minutes=45, workout=self.workout)
        self.leaderboard = Leaderboard.objects.create(team=self.team, user=self.user, total_minutes=45, total_distance=15.0, rank=1)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("profiles", response.data)
        self.assertIn("teams", response.data)
        self.assertIn("activities", response.data)
        self.assertIn("workouts", response.data)
        self.assertIn("leaderboard", response.data)

    def test_profiles_list(self):
        response = self.client.get("/api/profiles/")
        self.assertEqual(response.status_code, 200)

    def test_teams_list(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)

    def test_activities_list(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)

    def test_workouts_list(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)
