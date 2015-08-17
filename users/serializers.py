# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User

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