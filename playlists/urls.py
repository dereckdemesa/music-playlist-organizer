from django.urls import path
from .views import (playlist_list, playlist_create, playlist_detail,
                    playlist_update, playlist_delete)

urlpatterns = [
    path('', playlist_list, name='playlist_list'),
    path('create/', playlist_create, name='playlist_create'),
    path('<int:pk>/', playlist_detail, name='playlist_detail'),
    path('<int:pk>/update/', playlist_update, name='playlist_update'),
    path('<int:pk>/delete/', playlist_delete, name='playlist_delete'),
]
