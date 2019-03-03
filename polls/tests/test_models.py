from django.test import TestCase
from django.utils import timezone
from polls.models import Question
from unittest import skip

class QuestionModelTest(TestCase):

    def test_saving_and_retrieving_questions(self):
        first_question = Question.objects.create(question_text='Whats going on?', pub_date=timezone.now())
        second_question = Question.objects.create(question_text='What is the weather like?', pub_date=timezone.now())

        self.assertEqual(Question.objects.first(), first_question)
        saved_questions = Question.objects.all()
        self.assertEqual(saved_questions.count(), 2)
        self.assertEqual(saved_questions[0].question_text, 'Whats going on?')
        self.assertEqual(saved_questions[1].question_text, 'What is the weather like?')

class ChoiceModelTest(TestCase):
    

    def test_choice_related_to_question(self):  
        question = Question.objects.create(question_text='What is the weather like?', pub_date=timezone.now())
        choice = question.choice_set.create(choice_text='sunny',votes=0)
        self.assertIn(choice,question.choice_set.all())
        
        