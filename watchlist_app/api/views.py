from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

from watchlist_app.models import *
from watchlist_app.api.serializers import *

##### Stream
class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response (serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist :
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##### WatchList
class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist :
            return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##### BusinessType
class BusinessTypeAV(APIView):
    
    def get(self, request):
        movies = BusinessType.objects.all()
        serializer = BusinessTypeSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BusinessTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
class BusinessTypeDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = BusinessType.objects.get(pk=pk)
        except BusinessType.DoesNotExist :
            return Response({'error': 'BusinessType not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BusinessTypeSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = BusinessType.objects.get(pk=pk)
        serializer = BusinessTypeSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = BusinessType.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##### BusinessPlace
class BusinessPlaceAV(APIView):
    
    def get(self, request):
        movies = BusinessPlace.objects.all()
        serializer = BusinessPlaceSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BusinessPlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
class BusinessPlaceDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = BusinessPlace.objects.get(pk=pk)
        except BusinessPlace.DoesNotExist :
            return Response({'error': 'BusinessPlace not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BusinessPlaceSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = BusinessPlace.objects.get(pk=pk)
        serializer = BusinessPlaceSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = BusinessPlace.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##### Trip
class TripAV(APIView):
    
    def get(self, request):
        movies = Trip.objects.all()
        serializer = TripSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
class TripDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = Trip.objects.get(pk=pk)
        except Trip.DoesNotExist :
            return Response({'error': 'Trip not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TripSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = Trip.objects.get(pk=pk)
        serializer = TripSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = Trip.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##### BusinessPlacePicture
class BusinessPlacePictureAV(APIView):
    
    def get(self, request):
        movies = BusinessPlacePicture.objects.all()
        serializer = BusinessPlacePictureSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BusinessPlacePictureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors)
        
class BusinessPlacePictureDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = BusinessPlacePicture.objects.get(pk=pk)
        except BusinessPlacePicture.DoesNotExist :
            return Response({'error': 'BusinessPlacePicture not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BusinessPlacePictureSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = BusinessPlacePicture.objects.get(pk=pk)
        serializer = BusinessPlacePictureSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = BusinessPlacePicture.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET' :
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST' :
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else: 
        #     return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
    
#     if request.method == 'GET' :
        # try:
        #     movie = Movie.objects.get(pk=pk)
        # except Movie.DoesNotExist :
        #     return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        # serializer = MovieSerializer(movie)
        # return Response(serializer.data) 
    
#     if request.method == 'PUT' :
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE' :
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)