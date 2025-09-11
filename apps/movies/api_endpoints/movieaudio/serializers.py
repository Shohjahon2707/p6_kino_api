from rest_framework import serializers

from apps.movies.models import MovieAudio

from apps.movies.api_endpoints.language import MovieLanguageSerializer

class MovieAudioSerializer(serializers.ModelSerializer):
    language = MovieLanguageSerializer()

    class Meta:
        model = MovieAudio
        fields = ["id",'language']

__all__ = ["MovieAudioSerializer"]