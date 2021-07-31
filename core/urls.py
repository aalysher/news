from django.urls import path

from core import views


urlpatterns = [
    path('list/', views.NewsList.as_view()),
    path('detail/', views.NewsAllDetail.as_view()),
    path('news/', views.NewsListFlutter.as_view()),
    path('news/detail/', views.NewsDetailFlutter.as_view())
]

