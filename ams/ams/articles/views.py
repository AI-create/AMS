from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Article, Tag, AdminCode
from .serializers import ArticleSerializer, TagSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from django.views.generic import ListView, View
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Custom permission to check if the user is the author or is an admin
class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True
        return obj.author == request.user

# Article ViewSet
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Tag ViewSet
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.GET.get('is_admin') == 'true'
        return context

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ArticleCreateView(AdminRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(AdminRequiredMixin, UpdateView):
    model = Article
    template_name = 'articles/article_form.html'
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(AdminRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

@login_required
def role_selection_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'admin':
            return redirect('verify_admin_code')
        else:
            return redirect('article_list')
    return render(request, 'articles/role_selection.html')

@method_decorator(csrf_exempt, name='dispatch')
class AdminCodeVerificationView(View):
    def post(self, request, *args, **kwargs):
        admin_code = request.POST.get('admin_code')
        if AdminCode.objects.filter(code=admin_code).exists():
            # Redirect to articles list with admin privileges
            return JsonResponse({'redirect_url': '/?is_admin=true'}, status=200)
        return HttpResponseForbidden('Invalid admin code')
