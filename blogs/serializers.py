# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model= Blog
        read_only_fields = ('owner',)

class BlogListSerializer(BlogSerializer):

    class Meta(BlogSerializer.Meta):
        fields = ('id', 'title', 'resumen', 'urlImg', 'modified_at')

