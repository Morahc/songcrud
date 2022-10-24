from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Song, Artiste, Lyric
from .serializers import SongSerializer, ArtisteSerializer, LyricSerializer

# Create your views here.
class SongsViewset(ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer

class ArtisteViewset(ModelViewSet):
  queryset = Artiste.objects.all()
  serializer_class = ArtisteSerializer

class LyricViewset(ModelViewSet):
  queryset = Lyric.objects.all()
  serializer_class = LyricSerializer