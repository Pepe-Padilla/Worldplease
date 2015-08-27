# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from worldplease.settings import SELF_DOMAIN
import re

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        """
        Crea un a instancia de User a partir de los datos de validated_data que
        contiene valores deserializados
        :param validated_data: Diccionario de datos de usuario
        :return: Objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza la instancia de User con un validated_data
        :param instance: instancia de User
        :param validated_data: diccionario con los nuevos valores
        :return: User actualizado
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()

        return instance

    def validate_username(self, data):
        """
        Validación de que el nombre usario ya existe
        :param data: username
        :return: data si OK, raise si KO
        """
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError('Username already exists')
        elif self.instance:
            if self.instance.username != data:
                raise serializers.ValidationError("Can't change Username")
            else:
                return data
        else:
            matchobj = re.match(r'^([a-zA-Z]{1}[a-zA-Z0-9]*)$', data)
            if matchobj:
                return data
            else:
                raise serializers.ValidationError("Username must begin with a letter and contains only alphanumeric characteres")


class UserListSerializer(serializers.Serializer):
    username = serializers.CharField()
    user_page = serializers.SerializerMethodField(read_only=True)
    #user_page = serializers.CharField(source='username', read_only=True)

    def get_user_page(self, obj):
        return SELF_DOMAIN + reverse('blog_owner', args=[obj.username])