from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]