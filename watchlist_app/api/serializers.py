from rest_framework import serializers
from watchlist_app.models import *

class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta: 
        model = StreamPlatform
        fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = WatchList
        fields = "__all__"
        
class BusinessTypeSerializer(serializers.ModelSerializer):

    class Meta: 
        model = BusinessType
        fields = "__all__"
        
class BusinessPlaceSerializer(serializers.ModelSerializer):

    class Meta: 
        model = BusinessPlace
        fields = "__all__"

class TripSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Trip
        fields = "__all__"

# class WatchListSerializer(serializers.ModelSerializer):
    
#     len_name = serializers.SerializerMethodField()

#     class Meta:
#         model = MovieList
#         fields = '__all__'
#         # fields = ['id', 'name', 'description']
#         # exclude = ['name']
    
#     def get_len_name(self, object):
#         return len(object.name)
    
#     def validate(self, data):
#         if data['name'] == data['description']: 
#             raise serializers.ValidationError("Title and Description should be different!")
#         else: 
#             return data
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else :
#             return value



# def name_length(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Name is too short!")
    
#     if len(value) > 40:
#         raise serializers.ValidationError("Name is too Overflow!")
    
# def descripton_length(value):
#     if len(value) < 5:
#         raise serializers.ValidationError("Descripton is too short!")
    
#     if len(value) > 60:
#         raise serializers.ValidationError("Descripton is too Overflow!")

# class MovieSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(validators=[name_length])
    # description = serializers.CharField(validators=[name_length])
    # active = serializers.BooleanField()
    
    # def create(self, validated_data):
    #     return Movie.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.save()
    #     return instance
    
    # def validate(self, data):
    #     if data['name'] == data['description']: 
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else: 
    #         return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else :
    #         return value