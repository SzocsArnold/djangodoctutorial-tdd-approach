from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from polls.models import Question
from django.utils import timezone
class FunctionalTest(StaticLiveServerTestCase):
   
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path="C:\\Users\\Arnold\\Chromedriver\\chromedriver.exe")
    

    

    def create_pre_questions(self):
        question1 = Question.objects.create(question_text='What’s the weather like?', pub_date=timezone.now())
        question1.choice_set.create(choice_text='sunny')
        question1.choice_set.create(choice_text='cloudy')
        question2 = Question.objects.create(question_text='How are you feeling?', pub_date=timezone.now())
        question2.choice_set.create(choice_text='I’m all right')
        question2.choice_set.create(choice_text='A little depressed')