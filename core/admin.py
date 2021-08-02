from django.contrib import admin

from .models import NewsDetail, Filter, Lang, Image


class NewsSettings(admin.ModelAdmin):
    list_display = ('id', 'lang', 'filter', 'title')


admin.site.register(NewsDetail, NewsSettings)
admin.site.register(Filter)
admin.site.register(Lang)
admin.site.register(Image)
