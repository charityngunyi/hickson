from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
# Create your models here.

class Category(models.Model):
    # This class enables to create tender categories.
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Office(models.Model):
    # class enables to edit the tenders.
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='created')
    category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    capacity = models.PositiveIntegerField()
    availability = models.CharField(max_length=250)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='offices/%Y/%m/%d')
    # user = models.ForeignKey(User,related_name='owners', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='offices', on_delete=models.CASCADE)


    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title


class BidOffice(models.Model):
    CATEGORY_CHOICES = (
        ('organization', 'Organization'),
        ('business', 'Business'),
        ('school', 'School'),
    )
    APPROVAL_CHOICES = (
        ('not approved', 'Not Approved'),
        ('approved', 'Approved'),
        ('waiting', 'Waiting'),
    )
    BID_STATUS_CHOICES = [
        ('Selected', 'selected'),
        ('Waiting', 'waiting'),
        ('spaces_full', 'Spaces Full'),
    ]

    bid_status = models.CharField(
        max_length=20,
        choices=BID_STATUS_CHOICES,
        default='approved',
        )

    office = models.ForeignKey(Office, related_name='offices', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='biders', on_delete=models.CASCADE)
    office_purpose = models.CharField(max_length=250, choices=CATEGORY_CHOICES, default='business')
    bid = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    bid_approval = models.CharField(max_length=50, choices=APPROVAL_CHOICES, default='approved')
    comment = models.CharField(max_length=250, blank=True)

    class Meta:
        ordering = ('-bid',)

    def __str__(self):
        return self.office_purpose


class Amenities(models.Model):
    office = models.ForeignKey(Office, related_name='amenities', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['office'])
    class Meta:
        ordering = ['order']
    def __str__(self):
        return '{}. {}'.format(self.order, self.title)
# 

class Text(models.Model):
    amenity = models.ForeignKey(Amenities, related_name='texts', on_delete=models.CASCADE, default=1)
    content = models.TextField()

class File(models.Model):
    amenity = models.ForeignKey(Amenities, related_name='files', on_delete=models.CASCADE, default=1)
    file = models.FileField(upload_to='files')

class Image(models.Model):
    amenity = models.ForeignKey(Amenities, related_name='images', on_delete=models.CASCADE, default=1)
    file = models.FileField(upload_to='images')

class Video(models.Model):
    amenity = models.ForeignKey(Amenities, related_name='videos', on_delete=models.CASCADE, default=1)
    url = models.URLField()

