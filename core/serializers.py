from rest_framework import serializers

from core.models import NewsDetail, Image


class NewsCreateSerializer(serializers.ModelSerializer):
    """Serializer for create, update and delete news JS"""
    image = serializers.URLField()
    filter = serializers.CharField()
    lang = serializers.CharField()

    class Meta:
        model = NewsDetail
        fields = "__all__"


class NewsListSerializer(serializers.ModelSerializer):
    """List all news for JS"""
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


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for ordering and nested url Flutter"""
    class Meta:
        model = Image
        fields = ('url', 'order_num')


class NewsDetailFlutterSerializer(serializers.ModelSerializer):
    """Serializer for detail news Flutter"""
    image = ImageSerializer(many=True)

    class Meta:
        model = NewsDetail
        fields = ('header_title', 'text', 'add_date', 'image')
