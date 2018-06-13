from django.db import models
from django.contrib import admin
from django.template.response import TemplateResponse


from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class PromoPage(Page):
    body = StreamField([
        ('heroes', blocks.StaticBlock(
            admin_text='Heroes block: no configuration needed.',
            template='heroes.html')),
        ('index', blocks.RichTextBlock()),
        ('text_plus_screenshot', blocks.StreamBlock([
            ('screenshot', ImageChooserBlock()),
            ('text', blocks.RichTextBlock())
        ], template='text_plus_screenshot.html'))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['promotion'] = kwargs.get('promotion')
        return context

    def serve(self, request, *args, **kwargs):
        return TemplateResponse(
            request,
            self.get_template(request, *args, **kwargs),
            self.get_context(request, *args, **kwargs)
        )

    def get_site(self):
        return {'site_name': '8fit'}

    @property
    def url(self):
        return '/demo/%s' % self.slug

    @property
    def full_url(self):
        return self.url


class Promotion(models.Model):
    description = models.CharField(max_length=60)
    price = models.FloatField()
    discount = models.FloatField()

    def __str__(self):
        return self.description


class PromoUrl(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    promopage = models.ForeignKey(PromoPage, on_delete=models.CASCADE)


    def __str__(self):
        return '/promo/' + self.slug


admin.site.register(Promotion)
admin.site.register(PromoUrl)

