from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.movieaudio.serializers import MovieAudioSerializer
from apps.movies.models import MovieAudio


class MovieAudioDetailView(APIView):
    def get(self,request,pk):
        movie_audio = get_object_or_404(MovieAudio, id = pk)
        serializer = MovieAudioSerializer(movie_audio)
        return Response(serializer.data)
    
__all__= ["MovieAudioDetailView"]