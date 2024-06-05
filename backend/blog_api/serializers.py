from rest_framework import serializers
from .models import BlogPost, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['theme']


class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'created_on',
            'last_updated',
            'title',
            'body',
            'image',
            'image_caption',
            'tags'
        ]
