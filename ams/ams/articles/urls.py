from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, TagViewSet, role_selection_view, AdminCodeVerificationView, ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('role-selection/', role_selection_view, name='role_selection'),
    path('verify-admin-code/', AdminCodeVerificationView.as_view(), name='verify_admin_code'),
    path('api/', include(router.urls)),
]
