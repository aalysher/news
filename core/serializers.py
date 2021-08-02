from rest_framework import serializers

from core.models import NewsDetail, Image, Filter, Lang


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for ordering and nested url Flutter"""

    class Meta:
        model = Image
        fields = ('url', 'order_num')


class NewsCreateSerializer(serializers.ModelSerializer):
    """Serializer for create, update and delete news JS"""
    image = ImageSerializer(many=True)
    filter = serializers.CharField()
    lang = serializers.CharField()

    class Meta:
        model = NewsDetail
        fields = "__all__"

    def create(self, validated_data):
        lang = validated_data.pop('lang')
        filter = validated_data.pop('filter')
        images = validated_data.pop('image')

        lang_obj = Lang.objects.get(name=lang)
        filter_obj = Filter.objects.get(name=filter)
        news = NewsDetail.objects.create(filter=filter_obj,
                                         lang=lang_obj,
                                         **validated_data)

        for image in images:
            Image.objects.create(order_num=image['order_num'],
                                 url=image['url'],
                                 news_detail=news)

        return news

    def update(self, instance, validated_data):
        lang = validated_data.pop('lang')
        filter = validated_data.pop('filter')
        images = validated_data.pop('image')

        instance.title = validated_data['title']
        instance.header_title = validated_data['header_title']
        instance.filter = Filter.objects.get(name__iexact=filter)
        instance.lang = Lang.objects.get(name__iexact=lang)
        instance.save()
        return instance


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


class NewsDetailFlutterSerializer(serializers.ModelSerializer):
    """Serializer for detail news Flutter"""
    image = ImageSerializer(many=True)

    class Meta:
        model = NewsDetail
        fields = ('header_title', 'text', 'add_date', 'image')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for list category Flutter"""

    class Meta:
        model = Filter
        fields = ("name",)


class LanguageSerializer(serializers.ModelSerializer):
    """Serializer for list language Flutter"""

    class Meta:
        model = Lang
        fields = "__all__"
