from django.urls import reverse, resolve
from django.test import TestCase
from .views import home

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        """summary
        Testcase: Check if the status code of the response is 200
        ie: Get the home.html file and return
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Summary
        Testcase: Check if the path / matches with the view function home
        ie:Calls the home function
        """
        view = resolve('/')
        self.assertEqual(view.func, home)





# Create your tests here.
