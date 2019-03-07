from selenium import webdriver
from .base import FunctionalTest

class VotingTest(FunctionalTest):

    def test_can_vote(self):
        # pre creating some questions and choices
        self.create_pre_questions()

        self.browser.get(self.live_server_url)
        # User goes to home page and noticies a question and cliks on it
        self.browser.find_element_by_link_text('What’s the weather like?').click()
        self.browser.implicitly_wait(10)
        # then she notices the first option and she's voting for it
        self.browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()

        self.browser.find_elements_by_css_selector("input[type='submit'][value='Vote']")[0].click()
        self.browser.implicitly_wait(10)

        self.assertEqual(self.browser.find_element_by_link_text('Vote again?').text,
            'Vote again?')
        # She wants to vote again    
        self.browser.find_element_by_link_text('Vote again?').click()
        self.browser.implicitly_wait(10)
        # She clicks on the first choice again
        self.browser.find_elements_by_css_selector("input[type='radio'][value='1']")[0].click()
        # then She submits the form
        self.browser.find_elements_by_css_selector("input[type='submit'][value='Vote']")[0].click()
        self.browser.implicitly_wait(10)
    
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('sunny -- 2 votes', page_text)
        self.assertIn('cloudy -- 0 vote', page_text) 

