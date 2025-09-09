from rest_framework.views import APIView
from rest_framework.response import Response
from apps.movies.models import Genre
from .serializers import GenreListSerializer


class GenreListView(APIView):
    def get(self,request):
        genres = Genre.objects.all()
        serializer = GenreListSerializer(genres, many=True)

        return Response(serializer.data, status=200)

__all__=['GenreListView']