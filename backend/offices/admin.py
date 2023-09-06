from django.contrib import admin
from .models import Category, Office, BidOffice, Amenities, Text, File, Image, Video

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}

class AmenitiesInline(admin.StackedInline):
    model = Amenities


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'location', 'capacity', 'availability', 'price', 'user')
    list_filter = ('category', 'created', 'updated', 'user')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'location')
    inlines = [AmenitiesInline]  # Add Amenities as an inline

@admin.register(BidOffice)
class BidOfficeAdmin(admin.ModelAdmin):
    list_display = ('office', 'user', 'office_purpose', 'bid', 'bid_approval')
    list_filter = ('bid_approval', 'bid', 'user')
    search_fields = ('user__username', 'office_purpose')
 

