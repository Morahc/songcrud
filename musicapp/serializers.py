from rest_framework import serializers
from .models import Artiste, Lyric, Song


class ArtisteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Artiste
    fields = ['id', 'first_name', 'last_name', 'age']

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ['id', 'title', 'date_released', 'likes', 'artiste_id']

class SongUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = ['id', 'title', 'date_released', 'likes']

class LyricSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lyric
    fields = ['id', 'content', 'song_id']

class LyricUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lyric
    fields = ['id', 'content']

