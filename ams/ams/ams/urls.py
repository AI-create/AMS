from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet, TagViewSet, UserViewSet, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

router = DefaultRouter()
router.register(r'api/articles', ArticleViewSet, basename='article')
router.register(r'api/tags', TagViewSet, basename='tag')
router.register(r'api/users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('articles.urls')),
    path('api/', include(router.urls)),
]
