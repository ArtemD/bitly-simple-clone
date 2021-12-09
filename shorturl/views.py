from django.shortcuts import get_object_or_404, redirect
from shorturl.models import ShortUrl

def short2long(request, slug):
    url = get_object_or_404(ShortUrl, slug=slug)

    if url:
        return redirect(url.url)