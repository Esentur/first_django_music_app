from django.urls import path
from music_app.views import *

urlpatterns = [
    path('hello/',hello_world),
    path('get-music/',get_music),
    path('get-music/<int:id>/',music_detail ),
    path('patch-music/<int:id>/',music_patch ),
    path('music-create/',music_create),
    path('music-delete/<int:id>/',music_delete)
]