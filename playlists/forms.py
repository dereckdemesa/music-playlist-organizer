from django import forms
from .models import Playlist, Song

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'description', 'creator']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist']
