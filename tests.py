import json

from django.test import TestCase
from django.test import Client
from wagtail.core.models import Page

from home.models import Promotion, PromoUrl, PromoPage




class PromotionsTestCase(TestCase):

    def test_non_existing_promotion_page(self):
        c = Client()
        response = c.get('/promo/non-existing-promotion/')
        self.assertEqual(response.status_code, 404)

    def test_can_create_promotion_page_without_promotion(self):
        home = Page.objects.get(id=3)
        promo_page = PromoPage(title="test no promotion", body=json.dumps([{"value": None, "type": "heroes"}]))
        home.add_child(instance=promo_page)
        promo_page.save_revision().publish()
        c = Client()
        response = c.get(promo_page.url, follow=True)
        self.assertContains(response, u'Test promotion')


    def test_can_create_promotion_page_and_promotion(self):
        home = Page.objects.get(id=3)
        promo_page = PromoPage(title="test promotion", body=json.dumps([{"value": None, "type": "heroes"}]))
        home.add_child(instance=promo_page)
        promo_page.save_revision().publish()

        promo_price = 5
        promo_discount = 90
        promo_description = u'Super Profitable Promotion'

        promotion  = Promotion(description = promo_description, price=promo_price, discount = promo_discount)
        promotion.save()

        promo_url = PromoUrl(slug='test_url', promotion=promotion, promopage=promo_page)
        promo_url.save()

        c = Client()
        response = c.get(promo_url, follow=True)

        self.assertContains(response, promo_description)
        self.assertContains(response, u'%d%% OFF' % promo_discount)
        self.assertContains(response, u'Pay $%d now!' % promo_price)