from django.urls import path
from apps.movies.api_endpoints.genre.GenreList import GenreListView
from apps.movies.api_endpoints.movie.MovieDetail import MovieDetailView
from apps.movies.api_endpoints.movieaudio.views import MovieAudioDetailView
from apps.movies.api_endpoints.subtitle.views import MovieSubtitleView
from apps.movies.api_endpoints.moviefile.views import MovieFileView
from apps.movies.api_endpoints.watchsession.views import MovieWatchSessionView

urlpatterns = [
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("<int:pk>/", MovieDetailView.as_view(), name= "Movie_detail"),
    path('audios/<int:pk>/', MovieAudioDetailView.as_view(), name='Audios_list'),
    path("subtitles/<int:pk>/",MovieSubtitleView.as_view(), name='Subtitle'),
    path("moviefile/<int:pk>/",MovieFileView.as_view(), name="Movie-file"),
    path("watchsession/<int:pk>/",MovieWatchSessionView.as_view(), name="Watch-Session"),
]
