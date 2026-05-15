from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings

from pymongo import MongoClient

# Modelos simples para ejemplo, puedes expandirlos según necesidades reales
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Limpiar colecciones
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Equipos
        teams = [
            {'name': 'Marvel'},
            {'name': 'DC'}
        ]
        db.teams.insert_many(teams)

        # Usuarios
        users = [
            {'name': 'Spider-Man', 'email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Batman', 'email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'team': 'DC'}
        ]
        db.users.insert_many(users)
        db.users.create_index([('email', 1)], unique=True)

        # Actividades
        activities = [
            {'name': 'Running', 'user_email': 'spiderman@marvel.com', 'team': 'Marvel'},
            {'name': 'Cycling', 'user_email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Swimming', 'user_email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Yoga', 'user_email': 'wonderwoman@dc.com', 'team': 'DC'}
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {'user_email': 'spiderman@marvel.com', 'points': 120},
            {'user_email': 'ironman@marvel.com', 'points': 110},
            {'user_email': 'batman@dc.com', 'points': 130},
            {'user_email': 'wonderwoman@dc.com', 'points': 125}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {'name': 'Push Ups', 'description': 'Do 3 sets of 15 reps.'},
            {'name': 'Squats', 'description': 'Do 3 sets of 20 reps.'},
            {'name': 'Plank', 'description': 'Hold for 1 minute.'}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
