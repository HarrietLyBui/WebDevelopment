

from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #
        response = home_page(request) #what application returns after it has
        # done something with the request
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)


        self.assertTrue(response.content.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.strip().endswith('</html>'))