from math import ceil
from django.contrib.auth.models import User
from django.db.models import Count, Avg, Sum, F
from .models import Game

def generate_game_report():
    user_with_most_comments = User.objects.annotate(comment_count=Count('comments')).order_by('-comment_count').first().username
    highest_rated_game = Game.objects.annotate(total_rating=Sum('comments__like')).order_by('-total_rating').first().title
    average_likes_per_game = [{
            "title": game.title,
            "average_likes": ceil(game.average_likes)
    } for game in Game.objects.annotate(average_likes=Avg('comments__like'))]

    return {
        "user_with_most_comments": user_with_most_comments,
        "highest_rated_game": highest_rated_game,
        "average_likes_per_game": average_likes_per_game
    }
