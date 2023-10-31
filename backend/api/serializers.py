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
        fields = ('username', 'email', 'password', 'profile_type', 'first_name', 'last_name', 'Occupation_title', 'Occupation_description', 'photo', 'country', 'town', 'contacts', 'hobby')


# serializer for updating a user's profile
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', 'username')


class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 'profile_type', 'first_name', 'last_name', 'Occupation_title', 'Occupation_description', 'photo', 'country', 'town', 'contacts', 'hobby')

    def create(self, validated_data):
        # Remove 'confirm_password' from validated_data as it's not a model field
        confirm_password = validated_data.pop('confirm_password', None)

        if confirm_password and confirm_password != validated_data['password']:
            raise serializers.ValidationError("Passwords do not match")

        user = CustomUser.objects.create_user(**validated_data)
        return user



class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'Occupation_title', 'Occupation_description', 'photo', 'country', 'town', 'contacts', 'hobby')