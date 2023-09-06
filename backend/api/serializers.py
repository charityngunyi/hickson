# backend/api/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from offices.models import Category, Office, BidOffice, Amenities, Text, File, Image, Video
from users.models import CustomUser

# serializer for Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# serializer for Office model
class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


# serializer for BidOffice model
class BidOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidOffice
        fields = '__all__'

# serializer for Amenities model
class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = '__all__'


# serializer for Text model
class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


# serializer for File model
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


# serializer for Image model
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


# serializer for Video model
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'



# serializer for Profile model
class ProfileSerializer(serializers.ModelSerializer):
    
    # User profile that will describe blogers with attractive profile
    class Meta:
        model = CustomUser
        fields = '__all__'


# serializer for updating a user's profile
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', 'username')
