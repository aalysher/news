from rest_framework import serializers

from core.models import NewsDetail, Image


class NewsDetailSerializer(serializers.ModelSerializer):
    """Serializer CRUD for JS"""

    class Meta:
        model = NewsDetail
        fields = "__all__"


class NewsMainListSerializer(serializers.ModelSerializer):
    """Serializer for Main menu Flutter"""
    logo = serializers.URLField()

    class Meta:
        model = NewsDetail
        fields = ('title', 'logo')


class NewsDetailFlutterSerializer(serializers.ModelSerializer):
    """Serializer for detail news Flutter"""
    image = serializers.SlugRelatedField(slug_field='url', read_only=True, many=True)

    class Meta:
        model = NewsDetail
        fields = ('header_title', 'text', 'add_date', 'image')
