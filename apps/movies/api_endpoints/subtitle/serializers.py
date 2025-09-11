from rest_framework import serializers
from apps.movies.api_endpoints.language import MovieLanguageSerializer
from apps.movies.models import MovieSubtitle



class MovieSubtitleMiniSerializer(serializers.ModelSerializer):
    language = MovieLanguageSerializer()

    class Meta:
        model = MovieSubtitle
        fields = ['id','language']

__all__=["MovieSubtitleMiniSerializer"]