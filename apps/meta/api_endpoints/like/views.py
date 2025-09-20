from rest_framework.generics import CreateAPIView
from apps.meta.api_endpoints.like.serializers import MovieLikeSerializer

class MovieLikeView(CreateAPIView):
    serializer_class = MovieLikeSerializer
