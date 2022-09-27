from rest_framework import permissions
from .models import Category

class IsUserOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.company_set.count() == 0:
            return False
        elif not obj.company:
            return False
        else:
            return user.company_set.filter(pk=obj.company.id).count() == 1
        # return True
        # return user.company_set.filter(pk=obj.company.id).count()