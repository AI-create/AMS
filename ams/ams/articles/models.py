from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ['name']

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-created_at']

class AdminCode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Admin Code"
        verbose_name_plural = "Admin Codes"
        ordering = ['code']
