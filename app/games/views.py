from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
from .utils import generate_game_report

# Create your views here.
class GameViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=False, methods=['GET'])
    def report(self, request):
        return Response(generate_game_report())