from rest_framework import serializers
from apps.movies.models import Movie
from apps.movies.api_endpoints.subtitle.serializers import MovieSubtitleMiniSerializer
from apps.movies.api_endpoints.movieaudio.serializers import MovieAudioSerializer
from apps.movies.api_endpoints.country.serializers import MovieCountrySerializer
class MoviesDetailSerializer(serializers.ModelSerializer):
    moviesubtitle_set = MovieSubtitleMiniSerializer(many=True)
    movieaudio_set = MovieAudioSerializer(many=True)
    country = MovieCountrySerializer()
    class Meta:
        model = Movie
        fields = ['id', 'title', 'country', 'description',
                  'age_restriction', 'release_year', 'genres',
                  'moviesubtitle_set', 'movieaudio_set',
                  'posterimage_set', 'moviefile_set']

__all__ = ['MoviesDetailSerializer']
