# permissions/permissions.py
from rest_framework import permissions


"""
custom permission to allow read-only for all requests but for any write
requests for currently logged in user.
"""

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow write permissions only to editors or admins
        return request.user.is_authenticated and (
            request.user.is_superuser or
            request.user.groups.filter(name__in=['editor', 'admin']).exists()
        )

class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are allowed to the logged-in owner
        return request.user.is_authenticated and obj.user == request.user

class IsSeekerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Seekers are allowed read-only permissions for lists and retrieves
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Seekers are not allowed to create, update, or delete
        return request.user.is_authenticated and request.user.profile_type == 'seeker'

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Owners are allowed full permissions
        return request.user.is_authenticated and request.user.profile_type == 'owner'



class IsCustomUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are allowed to the logged-in user if the user is the owner of the profile
        return request.user.is_authenticated and request.user == obj  # Check if the user making the request is the owner of the profile
