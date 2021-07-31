from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import NewsDetail
from .serializers import NewsCreateSerializer, NewsMainListSerializer, NewsDetailFlutterSerializer, NewsListSerializer


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
    queryset = NewsDetail.objects.all()
    serializer_class = NewsMainListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['filter', 'lang']


class NewsDetailFlutter(generics.ListAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailFlutterSerializer
