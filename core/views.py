from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import NewsDetail, Filter, Lang
from .serializers import NewsCreateSerializer, NewsMainListSerializer, NewsDetailFlutterSerializer, NewsListSerializer, \
    CategorySerializer, LanguageSerializer


class NewsList(generics.ListCreateAPIView):
    """List and create news(JS)"""
    queryset = NewsDetail.objects.all()
    pagination_class = LimitOffsetPagination

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NewsListSerializer
        elif self.request.method == "POST":
            return NewsCreateSerializer


class NewsAllDetail(generics.RetrieveUpdateDestroyAPIView):
    """Get, update and delete(JS)"""
    queryset = NewsDetail.objects.all()
    serializer_class = NewsCreateSerializer


class NewsListFlutter(generics.ListAPIView):
    """List all news with filters"""
    queryset = NewsDetail.objects.all()
    serializer_class = NewsMainListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['filter', 'lang']


class NewsDetailFlutter(generics.RetrieveAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailFlutterSerializer


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang')
        queryset = Filter.objects.filter(lang__name=lang)
        return queryset

class LanguageList(generics.ListAPIView):
    queryset = Lang.objects.all()
    serializer_class = LanguageSerializer
