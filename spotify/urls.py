from django.urls import path
from .views import isSpotifyAuthView, spotify_request_token,SpotifyAuth
urlpatterns = [
    path('get-auth-url',SpotifyAuth.as_view()),
    path('is-spotify-auth',isSpotifyAuthView.as_view()),
    path('redirect',spotify_request_token)
]
