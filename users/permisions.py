# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    def has_permission(self, request, view):

        from users.api import UserListlAPI, UserDetailAPI

        if request.method == "POST":
            return True
        elif request.user.is_superuser:
            return True
        elif isinstance(view, UserListlAPI):
            return True
        else:
            return False


    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
