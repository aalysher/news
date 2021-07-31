from django.db import models


class Image(models.Model):
    url = models.URLField()
    news_detail = models.ForeignKey("NewsDetail", on_delete=models.CASCADE, related_name="image")
    order_num = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.news_detail)

    class Meta:
        ordering = ['order_num']


class NewsDetail(models.Model):
    title = models.CharField(max_length=255)
    header_title = models.CharField(max_length=255)
    text = models.TextField()
    filter = models.ForeignKey("Filter", on_delete=models.CASCADE, related_name='filter')
    add_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    lang = models.ForeignKey("Lang", on_delete=models.CASCADE, related_name='lang')

    def __str__(self):
        return self.title

    @property
    def logo(self):
        return Image.objects.filter(news_detail=self).first().url


class Filter(models.Model):
    name = models.CharField(max_length=255)
    lang = models.ForeignKey("Lang", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Lang(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
