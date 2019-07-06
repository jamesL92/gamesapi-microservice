from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)

class Platform(models.Model):
    name = models.CharField(max_length=20)


class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    age_rating = models.CharField(max_length=3, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games', null=True)
    platform = models.ManyToManyField(Platform, related_name='games')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message = models.CharField(max_length=100)
    created_date = models.DateField(default=timezone.now)
    like = models.PositiveIntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments')
