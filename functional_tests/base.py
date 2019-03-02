from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):
   
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:\\Users\\Arnold\\Chromedriver\\chromedriver.exe")
    

    def tearDown(self):
        self.browser.quit()