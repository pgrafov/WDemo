from django.http import HttpResponse, Http404
from home.models import PromoUrl, PromoPage


def show_promopage(request, slug):
    try:
        promourl = PromoUrl.objects.get(slug=slug)
    except PromoUrl.DoesNotExist:
        raise Http404
    return promourl.promopage.serve(request, promotion=promourl.promotion)

def show_promopage_demo(request, slug):
    try:
        promopage = PromoPage.objects.get(slug=slug)
    except PromoPage.DoesNotExist:
        raise Http404
    return promopage.serve(request)