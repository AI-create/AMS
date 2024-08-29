from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, callback

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/callback/', callback, name='auth_callback'),
]
