#-*-coding: utf-8-*-

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Tag, Article

class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = Category
        fields = (
            'url', 'id', 'name', 'articles',
            'created_time', 'last_modified_time'
        )

class TagSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = Tag
        fields = (
            'url', 'id', 'name', 'articles',
            'created_time', 'last_modified_time'
        )

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    #category = serializers.ReadOnlyField(source='category.name')
    #tags = serializers.HyperlinkedRelatedField(many=True, view_name='tag-detail', read_only=True)
    bg_img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = (
            'url', 'id', 'bg_img', 'title', 'abstract', 'body',
            'created_time', 'last_modified_time', 'status',
            'topped', 'views', 'category', 'tags', 'owner')
        read_only_fields = (
            'url', 'id', 'bg_img')

class UserSerializer(serializers.ModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = (
            'url', 'id', 'username', 'articles'
        )
