from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'tags', 'author']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        article = Article.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            article.tags.add(tag)
        return article

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
