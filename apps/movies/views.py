from django.shortcuts import render

# Create your views here.from rest_framework import generics
from rest_framework import generics
from .models import Genre, Language, Movie, MovieAudio, MovieSubtitle, PosterImage, MovieFile
from .serializers import (
    GenreSerializer, LanguageSerializer, MovieSerializer,
    MovieAudioSerializer, MovieSubtitleSerializer,
    PosterImageSerializer, MovieFileSerializer
)

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
class LanguageListCreateView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
class MovieAudioListCreateView(generics.ListCreateAPIView):
    queryset = MovieAudio.objects.all()
    serializer_class = MovieAudioSerializer
class MovieAudioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieAudio.objects.all()
    serializer_class = MovieAudioSerializer
class MovieSubtitleListCreateView(generics.ListCreateAPIView):
    queryset = MovieSubtitle.objects.all()
    serializer_class = MovieSubtitleSerializer

class MovieSubtitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieSubtitle.objects.all()
    serializer_class = MovieSubtitleSerializer

class PosterImageListCreateView(generics.ListCreateAPIView):
    queryset = PosterImage.objects.all()
    serializer_class = PosterImageSerializer

class PosterImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PosterImage.objects.all()
    serializer_class = PosterImageSerializer

class MovieFileListCreateView(generics.ListCreateAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer

class MovieFileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieFile.objects.all()
    serializer_class = MovieFileSerializer
