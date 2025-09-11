from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.moviefile.serializers import MovieFileSerializer
from apps.movies.models import MovieFile

class MovieFileView(APIView):
    def get(self,request, pk):
        movie = get_object_or_404(MovieFile, id=pk)
        serializer = MovieFileSerializer(movie)
        return Response(serializer.data)
    
__all__= ["MovieFileView"]
