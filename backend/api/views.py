from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated
from offices.models import Category, Office, BidOffice, Amenities, Text, File, Image, Video
from users.models import CustomUser
from .serializers import CategorySerializer, OfficeSerializer, BidOfficeSerializer, AmenitiesSerializer, ProfileUpdateSerializer
from .serializers import TextSerializer, FileSerializer, ImageSerializer, VideoSerializer, ProfileSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly, IsSeekerOrReadOnly, IsUserOrReadOnly, IsCustomUserOrReadOnly
# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
# 
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Create 
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = CategorySerializer


# Retrieve

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAdminOrReadOnly, )
    serializer_class = CategorySerializer


# 
class OfficeListAPIView(ListAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


# Create 
class OfficeCreateAPIView(CreateAPIView):
    queryset = Office.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = OfficeSerializer

# Retrieve offices details
class OfficeDetailAPIView(RetrieveAPIView):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer


# 
class OfficeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = OfficeSerializer


# 
class BidOfficeListAPIView(ListAPIView):
    queryset = BidOffice.objects.all()
    serializer_class = BidOfficeSerializer


# Create 
class BidOfficeCreateAPIView(CreateAPIView):
    queryset = BidOffice.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = BidOfficeSerializer


# 
class BidOfficeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BidOffice.objects.all()
    permission_classes = (IsUserOrReadOnly, IsSeekerOrReadOnly, IsAdminOrReadOnly)
    serializer_class = BidOfficeSerializer


# 
class AmenitiesListAPIView(ListAPIView):
    queryset = Amenities.objects.all()
    serializer_class = AmenitiesSerializer


# Create 
class AmenitiesCreateAPIView(CreateAPIView):
    queryset = Amenities.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly)
    serializer_class = AmenitiesSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class AmenitiesRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Amenities.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsUserOrReadOnly, IsAdminOrReadOnly)
    serializer_class = AmenitiesSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class TextListAPIView(ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


# Create 
class TextCreateAPIView(CreateAPIView):
    queryset = Text.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = TextSerializer


# 
class TextRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Text.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsUserOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = TextSerializer


# 
class FileListAPIView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


# Create 
class FileCreateAPIView(CreateAPIView):
    queryset = File.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class FileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsUserOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Create 
class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class ImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsUserOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class VideoListAPIView(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


# Create 
class VideoCreateAPIView(CreateAPIView):
    queryset = Video.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAdminOrReadOnly)
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class VideoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsUserOrReadOnly, IsAdminOrReadOnly,)
    serializer_class = VideoSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class ProfileListAPIView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer


# Create 
class ProfileCreateAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)


# 
class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsCustomUserOrReadOnly,)
    serializer_class = ProfileUpdateSerializer
    parser_classes = (MultiPartParser, FormParser)
