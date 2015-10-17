# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer, UserListSerializer
#from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from users.permisions import UserPermission, UserListPermission

class UserListlAPI(GenericAPIView):

    permission_classes = (UserPermission,)

    def get(self, request):
        username_str = request.GET.get('username', None)
        if username_str:
            users = User.objects.filter(username__contains=username_str).order_by('username')
            #serializer = UserListSerializer(users, many=True)
        else:
            users = User.objects.all().order_by('username')
            #serializer = UserSerializer(users, many=True)

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(GenericAPIView):

    permission_classes = (UserListPermission,)

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        self.check_object_permissions(request, user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

