from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import *

urlpatterns = [
    path('movie/', WatchListAV.as_view(), name="movie-list"),
    path('movie/<int:pk>', WatchDetailAV.as_view(), name="movie-detail"),
    
    path('stream/', StreamPlatformAV.as_view(), name="stream"),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="stream-detail"),
]