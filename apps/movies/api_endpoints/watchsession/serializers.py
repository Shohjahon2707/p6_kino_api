from rest_framework import serializers
from apps.movies.models import WatchSession
from apps.movies.api_endpoints.language.serializers import MovieLanguageSerializer
from apps.movies.api_endpoints.subtitle.serializers import MovieSubtitleMiniSerializer

class MovieWatchSessionSerializer(serializers.ModelSerializer):
    language=MovieLanguageSerializer
    subtitle=MovieSubtitleMiniSerializer

    class Meta:
        model=WatchSession
        fields="__all__"

__all__=["MovieWatchSessionSerializer"]