#-*-coding: utf-8-*-

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'api/categories', views.CategoryViewSet)
router.register(r'api/tags', views.TagViewSet)
router.register(r'api/articles', views.ArticleViewSet)
router.register(r'api/users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)