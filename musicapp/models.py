from django.db import models

# Create your models here.
class Artiste(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  age = models.IntegerField()

  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name}'

class Song(models.Model):
  title = models.CharField(max_length=200)
  date_released = models.DateField()
  likes = models.IntegerField()
  artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.title

class Lyric(models.Model):
  content = models.TextField()
  song_id = models.ForeignKey(Song, on_delete=models.CASCADE)