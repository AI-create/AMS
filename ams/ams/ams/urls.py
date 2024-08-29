from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet, callback

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Register API routes with the router
    path('auth/callback/', callback, name='auth_callback'),  # Auth0 callback URL
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 URL configuration
]
