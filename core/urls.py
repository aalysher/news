from django.urls import path

from core import views


urlpatterns = [
    path('list/', views.NewsList.as_view()),
    path('detail/<int:pk>/', views.NewsAllDetail.as_view()),
    path('news/', views.NewsListFlutter.as_view()),
    path('news/<int:pk>/', views.NewsDetailFlutter.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('language/', views.LanguageList.as_view())

]

