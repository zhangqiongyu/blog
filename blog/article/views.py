# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework import viewsets, permissions, mixins, parsers, status
from rest_framework.decorators import detail_route, parser_classes
from rest_framework.response import Response

from .models import Category, Tag, Article
from .serializers import CategorySerializer, TagSerializer, ArticleSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
"""
class ArticleViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def __init__(self, *args, **kwargs):
        super(ArticleViewSet, self).__init__(*args, **kwargs)

    @detail_route(methods=['POST'], permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
    @parser_classes((parsers.FormParser, parsers.MultiPartParser,))
    def post_background_image(self, request, *args, **kwargs):
        if 'upload' in request.data:
            article = self.get_object()
            article.bg_img.delete()

            upload = request.data['upload']
            article.bg_img.save(upload.name, upload)
            return Response(status=status.HTTP_201_CREATED, headers={'Location': article.bg_img.url})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

