
from functional_tests.base import FunctionalTest

class HomePageTest(FunctionalTest):

    def test_server(self):
        self.browser.get('http://localhost:8000')