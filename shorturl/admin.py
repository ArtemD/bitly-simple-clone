from django.contrib import admin
from shorturl.models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    pass

admin.site.register(ShortUrl, ShortUrlAdmin)