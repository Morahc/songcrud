from rest_framework.viewsets import ModelViewSet
from .models import Song, Artiste, Lyric
from .serializers import LyricUpdateSerializer, SongSerializer, ArtisteSerializer, LyricSerializer, SongUpdateSerializer

# Create your views here.
class SongsViewset(ModelViewSet):
  queryset = Song.objects.all()
  
  def get_serializer_class(self):
    if self.action == 'update':
      return SongUpdateSerializer
    return SongSerializer

class ArtisteViewset(ModelViewSet):
  queryset = Artiste.objects.all()
  serializer_class = ArtisteSerializer

class LyricViewset(ModelViewSet):
  queryset = Lyric.objects.all()

  def get_serializer_class(self):
    if self.action == 'update':
      return LyricUpdateSerializer
    return LyricSerializer