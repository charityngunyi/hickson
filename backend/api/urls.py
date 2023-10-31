# portfolio/urls.py
from django.urls import path
from .views import (
    CategoryListAPIView, CategoryCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    OfficeListAPIView, OfficeCreateAPIView, OfficeRetrieveUpdateDestroyAPIView,
    BidOfficeListAPIView, BidOfficeCreateAPIView, BidOfficeRetrieveUpdateDestroyAPIView,
    AmenitiesListAPIView, AmenitiesCreateAPIView, AmenitiesRetrieveUpdateDestroyAPIView,
    TextListAPIView, TextCreateAPIView, TextRetrieveUpdateDestroyAPIView,
    FileListAPIView, FileCreateAPIView, FileRetrieveUpdateDestroyAPIView,
    ImageListAPIView, ImageCreateAPIView, ImageRetrieveUpdateDestroyAPIView,
    VideoListAPIView, VideoCreateAPIView, VideoRetrieveUpdateDestroyAPIView,
    ProfileListAPIView, ProfileCreateAPIView, ProfileRetrieveUpdateDestroyAPIView,
    CategoryDetailAPIView, OfficeDetailAPIView, CustomUserCreateView, CustomUserUpdateView
)

urlpatterns = [
path(
    route='category',
    view=CategoryListAPIView.as_view(),
    name='category_view'
    ),
# create
path(
    route='category/create',
    view=CategoryCreateAPIView.as_view(),
    name='category_create'
    ),
# detail
path(
    route='category/detail/<int:pk>/',
    view=CategoryDetailAPIView.as_view(),
    name='category_deatil'
    ),
# /api/:uuid/
path(
    route='category/<int:pk>/',
    view=CategoryRetrieveUpdateDestroyAPIView.as_view(),
    name='category_edit_delete'
    ),
path(
    route='office',
    view=OfficeListAPIView.as_view(),
    name='office_view'
    ),
# create
path(
    route='office/create',
    view=OfficeCreateAPIView.as_view(),
    name='office_create'
    ),
# office details
path(
    route='office/detail/<int:pk>/',
    view=OfficeDetailAPIView.as_view(),
    name='office_detail'
    ),
# /api/:uuid/
path(
    route='office/<int:pk>/',
    view=OfficeRetrieveUpdateDestroyAPIView.as_view(),
    name='office_edit_delete'
    ),
path(
    route='bidoffice',
    view=BidOfficeListAPIView.as_view(),
    name='bidoffice_view'
    ),
# create
path(
    route='bidoffice/create',
    view=BidOfficeCreateAPIView.as_view(),
    name='bidoffice_create'
    ),
# /api/:uuid/
path(
    route='bidoffice/<int:pk>/',
    view=BidOfficeRetrieveUpdateDestroyAPIView.as_view(),
    name='bidoffice_edit_delete'
    ),
path(
    route='amenities',
    view=AmenitiesListAPIView.as_view(),
    name='amenities_view'
    ),
# create
path(
    route='amenities/create',
    view=AmenitiesCreateAPIView.as_view(),
    name='amenities_create'
    ),
# /api/:uuid/
path(
    route='amenities/<int:pk>/',
    view=AmenitiesRetrieveUpdateDestroyAPIView.as_view(),
    name='amenities_edit_delete'
    ),
path(
    route='text',
    view=TextListAPIView.as_view(),
    name='text_view'
    ),
# create
path(
    route='text/create',
    view=TextCreateAPIView.as_view(),
    name='text_create'
    ),
# /api/:uuid/
path(
    route='text/<int:pk>/',
    view=TextRetrieveUpdateDestroyAPIView.as_view(),
    name='text_edit_delete'
    ),
path(
    route='file',
    view=FileListAPIView.as_view(),
    name='file_view'
    ),
# create
path(
    route='file/create',
    view=FileCreateAPIView.as_view(),
    name='file_create'
    ),
# /api/:uuid/
path(
    route='file/<int:pk>/',
    view=FileRetrieveUpdateDestroyAPIView.as_view(),
    name='file_edit_delete'
    ),
path(
    route='image',
    view=ImageListAPIView.as_view(),
    name='image_view'
    ),
# create
path(
    route='image/create',
    view=ImageCreateAPIView.as_view(),
    name='image_create'
    ),
# /api/:uuid/
path(
    route='image/<int:pk>/',
    view=ImageRetrieveUpdateDestroyAPIView.as_view(),
    name='image_edit_delete'
    ),
path(
    route='video',
    view=VideoListAPIView.as_view(),
    name='video_view'
    ),
# create
path(
    route='video/create',
    view=VideoCreateAPIView.as_view(),
    name='video_create'
    ),
# /api/:uuid/
path(
    route='video/<int:pk>/',
    view=VideoRetrieveUpdateDestroyAPIView.as_view(),
    name='video_edit_delete'
    ),
path(
    route='profile',
    view=ProfileListAPIView.as_view(),
    name='profile_view'
    ),
# create
path(
    route='profile/create',
    view=ProfileCreateAPIView.as_view(),
    name='profile_create'
    ),
# /api/:uuid/
path(
    route='profile/<int:pk>/',
    view=ProfileRetrieveUpdateDestroyAPIView.as_view(),
    name='profile_edit_delete'
    ),
# user create
path(
    route='profile/user/create',
    view=CustomUserCreateView.as_view(),
    name='user_create'
    ),
# update
path(
    route='profile/user/update/<int:pk>/',
    view=CustomUserUpdateView.as_view(),
    name='user_update'
    ),
]