from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details

from watchlist_app.api.views import *

urlpatterns = [
    path('movie/', WatchListAV.as_view(), name="movie-list"),
    path('movie/<int:pk>', WatchDetailAV.as_view(), name="movie-detail"),
    
    path('stream/', StreamPlatformAV.as_view(), name="stream"),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="stream-detail"),
    
    path('BusinessType/', BusinessTypeAV.as_view(), name="BusinessType"),
    path('BusinessType/<int:pk>', BusinessTypeDetailAV.as_view(), name="BusinessType-detail"),
    
    path('BusinessPlace/', BusinessPlaceAV.as_view(), name="BusinessPlace"),
    path('BusinessPlace/<int:pk>', BusinessPlaceDetailAV.as_view(), name="BusinessPlace-detail"),
    
    path('Trip/', TripAV.as_view(), name="Trip"),
    path('Trip/<int:pk>', TripDetailAV.as_view(), name="Trip-detail"),
]