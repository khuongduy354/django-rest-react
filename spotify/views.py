from django.shortcuts import render

# Create your views here.
from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from rest_framework.views import APIView
from requests import Request, post
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
from rest_framework.response import Response
# from .util import update_or_create_user_tokens, is_spotify_authenticated, get_user_tokens, execute_spotify_api_call
from .models import SpotifyToken
from .utils import isSpotifyAuth,getToken,update_or_create_user_tokens,refreshToken
# Create your views here.
class SpotifyAuth(APIView):
    def get(self,request,format=None):
        scope = 'user-read-playback-state user-modify-playback-state user-read-currently-playing'
        url=Request('GET','https://accounts.spotify.com/authorize',params={
            'scope':scope,
            'response-type':'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url
        return Response({'url':url},status=status.HTTP_200_OK)


def spotify_request_token(request):
    code= request.GET.get('code')
    response=post('https://accounts.spotify.com/api/token',data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    if not request.session.exists(request.session.session_key):
        request.session.create()
    session_id=request.session.session_key
    update_or_create_user_tokens(session_id=session_id, access_token=access_token,token_type=token_type,refresh_token=refresh_token,expires_in=expires_in) 
    return HttpResponseRedirect('frontend')

class isSpotifyAuthView(APIView):
    def get(self,request,format=None):
        isAuth=isSpotifyAuth(self.request.session.session_key)
        return Response({'status':isAuth},status=status.HTTP_200_OK)
            