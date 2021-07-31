from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import NewsDetail
from .serializers import NewsDetailSerializer, NewsMainListSerializer, NewsDetailFlutterSerializer


class NewsList(generics.ListCreateAPIView):
    """List and create news(JS)"""
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer
    pagination_class = LimitOffsetPagination


class NewsAllDetail(generics.RetrieveUpdateDestroyAPIView):
    """Get, update and delete(JS)"""
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer


class NewsListFlutter(generics.ListAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsMainListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['filter', 'lang']


class NewsDetailFlutter(generics.ListAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailFlutterSerializer
