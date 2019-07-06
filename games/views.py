from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
