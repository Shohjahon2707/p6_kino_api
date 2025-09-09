from django.urls import path
from .views import (
    GenreListCreateView, GenreDetailView,
    LanguageListCreateView, LanguageDetailView,
    MovieListCreateView, MovieDetailView,
    MovieAudioListCreateView, MovieAudioDetailView,
    MovieSubtitleListCreateView, MovieSubtitleDetailView,
    PosterImageListCreateView, PosterImageDetailView,
    MovieFileListCreateView, MovieFileDetailView
)

urlpatterns = [
    path("genres/", GenreListCreateView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("languages/", LanguageListCreateView.as_view(), name="language-list"),
    path("languages/<int:pk>/", LanguageDetailView.as_view(), name="language-detail"),
    path("", MovieListCreateView.as_view(), name="movie-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path("audios/", MovieAudioListCreateView.as_view(), name="audio-list"),
    path("audios/<int:pk>/", MovieAudioDetailView.as_view(), name="audio-detail"),
    path("subtitles/", MovieSubtitleListCreateView.as_view(), name="subtitle-list"),
    path("subtitles/<int:pk>/", MovieSubtitleDetailView.as_view(), name="subtitle-detail"),
    path("posters/", PosterImageListCreateView.as_view(), name="poster-list"),
    path("posters/<int:pk>/", PosterImageDetailView.as_view(), name="poster-detail"),
    path("files/", MovieFileListCreateView.as_view(), name="file-list"),
    path("files/<int:pk>/", MovieFileDetailView.as_view(), name="file-detail"),
]
