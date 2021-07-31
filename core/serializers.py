from rest_framework import serializers

from core.models import NewsDetail, Image


class NewsCreateSerializer(serializers.ModelSerializer):
    image = serializers.URLField()
    filter = serializers.CharField()
    lang = serializers.CharField()

    class Meta:
        model = NewsDetail
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    logo = serializers.URLField()

    class Meta:
        model = NewsDetail
        fields = ('title', 'logo', 'add_date')


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
