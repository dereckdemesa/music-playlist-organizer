from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists', null=True)


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    playlists = models.ManyToManyField(Playlist, related_name='songs')

def __str__(self):
    return self.title  # For Song

def __str__(self):
    return self.name  # For Playlist

