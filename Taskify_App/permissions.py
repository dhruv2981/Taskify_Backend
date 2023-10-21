from rest_framework import permissions

class isAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role=='a'
        



