from rest_framework import serializers

from apps.movies.models import MovieFile


class MovieFileSerializer(serializers.ModelSerializer):


    class Meta:
        model = MovieFile
        fields = '__all__'

__all__=["MovieFileSerializer"]