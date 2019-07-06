from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, null=True, blank=True)
    age_rating = models.CharField(max_length=3, null=True, blank=True)
    likes = models.PositiveIntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games', null=True)
