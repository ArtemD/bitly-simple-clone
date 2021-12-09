from django.http import response
from django.test import TestCase

class ShortUrlTestCase(TestCase):
    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertEquals(response.status_code, 302)