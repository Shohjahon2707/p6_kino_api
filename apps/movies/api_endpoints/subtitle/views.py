from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.subtitle.serializers import MovieSubtitleMiniSerializer
from apps.movies.models import MovieSubtitle



class MovieSubtitleView(APIView):
    def get(self,request,pk):
        movie_subtitle = get_object_or_404(MovieSubtitle, id = pk)
        serializer = MovieSubtitleMiniSerializer(movie_subtitle)
        return Response(serializer.data)
__all__=["MovieSubtitleView"]