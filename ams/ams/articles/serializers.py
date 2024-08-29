from rest_framework import serializers
from .models import Article, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'tags']

    def create(self, validated_data):
        tags_data = self.context['request'].data.get('tags')
        article = Article.objects.create(**validated_data)
        if tags_data:
            for tag in tags_data:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                article.tags.add(tag_obj)
        return article

    def update(self, instance, validated_data):
        tags_data = self.context['request'].data.get('tags')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        if tags_data:
            instance.tags.clear()
            for tag in tags_data:
                tag_obj, created = Tag.objects.get_or_create(name=tag)
                instance.tags.add(tag_obj)

        return instance
