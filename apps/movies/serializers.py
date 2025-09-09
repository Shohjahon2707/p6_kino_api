from rest_framework import serializers
from .models import Genre, Language, Movie, MovieAudio, MovieSubtitle, PosterImage, MovieFile


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    genres_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, write_only=True, source="genres"
    )

    class Meta:
        model = Movie
        fields = [
            "id", "title", "country", "description", "age_restriction",
            "release_year", "genres", "genres_ids"
        ]


class MovieAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieAudio
        fields = "__all__"


class MovieSubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSubtitle
        fields = "__all__"


class PosterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosterImage
        fields = "__all__"


class MovieFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFile
        fields = "__all__"
