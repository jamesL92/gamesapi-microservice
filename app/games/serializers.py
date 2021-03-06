from rest_framework import serializers
from .models import Game, Comment

class CommentSerializer(serializers.ModelSerializer):
    dateCreated = serializers.DateField(source='created_date')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Comment
        fields = (
            'user',
            'message',
            'dateCreated',
            'like'
        )
        read_only_fields = fields

class GameSerializer(serializers.ModelSerializer):

    by = serializers.CharField(source='publisher.name')
    platform = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = (
            'title',
            'description',
            'by',
            'age_rating',
            'likes',
            'platform',
            'comments',
        )
        read_only_fields = fields
