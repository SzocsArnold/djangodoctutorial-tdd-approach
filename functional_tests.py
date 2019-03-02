from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):
   
    
    def setUp(self):
       self.browser = webdriver.Firefox(executable_path="C:\\Users\\Arnold\\geckodriver\\geckodriver.exe")
    
    def test_django(self):
        self.browser.get('http://localhost:8000')
