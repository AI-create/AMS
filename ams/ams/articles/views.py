from django.shortcuts import redirect
from django.contrib.auth import login
from django.conf import settings
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Tag
from .serializers import ArticleSerializer, TagSerializer
import requests
from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, TokenHasReadWriteScope
from django.db.models import Q

# Auth0 callback view
def callback(request):
    code = request.GET.get('code')
    token_url = f"https://{settings.AUTH0_DOMAIN}/oauth/token"
    token_payload = {
        'client_id': settings.AUTH0_CLIENT_ID,
        'client_secret': settings.AUTH0_CLIENT_SECRET,
        'redirect_uri': settings.AUTH0_CALLBACK_URL,
        'code': code,
        'grant_type': 'authorization_code',
    }
    token_info = requests.post(token_url, data=token_payload).json()
    user_url = f"https://{settings.AUTH0_DOMAIN}/userinfo"
    user_info = requests.get(user_url, headers={'Authorization': f"Bearer {token_info['access_token']}"}).json()
    
    user, _ = User.objects.get_or_create(username=user_info['email'])
    login(request, user)
    return redirect('/')

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin users to create, update, or delete articles.
    Authenticated users can only read.
    """

    def has_permission(self, request, view):
        # Allow read-only access for authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Write permissions are only allowed to the admin users
        return request.user.is_staff

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAdminOrReadOnly, TokenHasReadWriteScope]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(ArticleViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != request.user:
            return Response({"detail": "You do not have permission to edit this article."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != request.user:
            return Response({"detail": "You do not have permission to delete this article."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

    # GET /articles/{id}/tags/ (list tags of an article)
    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def tags(self, request, pk=None):
        article = self.get_object()
        tags = article.tags.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    # Custom search functionality
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def search(self, request):
        query = request.query_params.get('q', '')
        if query:
            articles = self.queryset.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) | 
                Q(tags__name__icontains=query)
            ).distinct()
        else:
            articles = self.queryset.none()
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)
