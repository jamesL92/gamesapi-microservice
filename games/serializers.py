from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):

    by = serializers.CharField(source='publisher.name')
    class Meta:
        model = Game
        fields = (
            'name',
            'description',
            'by',
            'age_rating',
            'likes',
        )