from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Test Team')
        self.assertEqual(str(user), 'test@example.com')

    def test_create_activity(self):
        activity = Activity.objects.create(name='Test Activity', user_email='test@example.com', team='Test Team')
        self.assertIn('Test Activity', str(activity))

    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', points=42)
        self.assertIn('test@example.com', str(lb))

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(str(workout), 'Test Workout')
