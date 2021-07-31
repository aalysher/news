from django.contrib import admin

from .models import NewsDetail, Filter, Lang, Image

admin.site.register(NewsDetail)
admin.site.register(Filter)
admin.site.register(Lang)
admin.site.register(Image)