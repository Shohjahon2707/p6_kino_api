from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.movies.api_endpoints.watchsession.serializers import MovieWatchSessionSerializer
from apps.movies.models import WatchSession

class MovieWatchSessionView(APIView):
    def get(self,request,pk):
        movie_watch = get_object_or_404(WatchSession, id = pk)
        serializer = MovieWatchSessionSerializer(movie_watch)
        return Response(serializer.data)
__all__ = ["MovieWatchSessionView"]