from django.db import models

class ShortUrl(models.Model):
    url = models.URLField(max_length=2000, help_text='Long url')
    slug = models.SlugField(max_length=100, primary_key=True, help_text='Easy to remember short url')
    hits = models.PositiveIntegerField(default=0)