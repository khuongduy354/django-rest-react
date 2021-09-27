from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID,CLIENT_SECRET,REDIRECT_URI
from requests import post

def getToken(session_id): 
    token= SpotifyToken.objects.filter(user=session_id)
    if token:
        return token[0]
    else:
        return None
def isSpotifyAuth(session_id): 
    token= getToken(session_id)
    if token: 
        if token.expires_in <= timezone.now():
            refreshToken(session_id=session_id) 
        return True
    return False

def update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token):
    tokens=getToken(session_id)
    expires_in = timezone.now() + timedelta(seconds=expires_in)

    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_fields=['access_token',
                                   'refresh_token', 'expires_in', 'token_type'])
    else:
        tokens = SpotifyToken(user=session_id, access_token=access_token,
                              refresh_token=refresh_token, token_type=token_type, expires_in=expires_in)
        tokens.save()

def refreshToken(session_id):
    refresh_token=getToken(session_id)
    response=post('https://accounts.spotify.com/api/token',data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()
    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')
    update_or_create_user_tokens(access_token=access_token,token_type=token_type,expires_in=expires_in,refresh_token=refresh_token)

