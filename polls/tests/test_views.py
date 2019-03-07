from django.test import TestCase
from polls.models import Question
from django.utils import timezone
from django.urls import reverse

class IndexPageTest(TestCase):

    def test_index_page_diplays_questions(self):
        Question.objects.create(question_text='What is the time?',pub_date=timezone.now())
        response = self.client.get('/')
        self.assertContains(response, 'What is the time?')
    
    def test_index_page_displays_only_five_latest_questions(self):
        Question.objects.create(question_text='What is the time?', pub_date=timezone.now())
        Question.objects.create(question_text='hello?', pub_date=timezone.now())
        Question.objects.create(question_text='waoo?', pub_date=timezone.now())
        Question.objects.create(question_text='who?', pub_date=timezone.now())
        Question.objects.create(question_text='what?', pub_date=timezone.now())
        Question.objects.create(question_text='This?', pub_date=timezone.now())
        response = self.client.get('/')
        self.assertEqual(response.context['latest_question_list'].count(), 5)

class DetailPageTest(TestCase):

    def test_display_choices_for_a_particular_question(self):

        correct_question = Question.objects.create(question_text='What do you do?', pub_date=timezone.now())
        correct_question.choice_set.create(choice_text='I am unemployed')
        correct_question.choice_set.create(choice_text ='I work in a bank')
        other_question = Question.objects.create(question_text='Are you married?', pub_date=timezone.now())
        other_question.choice_set.create(choice_text='Yes, i have been married for two years now')

        response = self.client.get(f'/polls/{correct_question.id}/')
        self. assertTemplateUsed(response, 'detail.html')
        self.assertContains(response, 'I am unemployed')
        self.assertContains(response, 'I work in a bank')
        self.assertNotContains(response, 'Yes, i have been married for two years now')

    def test_question_does_not_exist(self):
        response = self.client.get(f'/polls/5/')
        self.assertEqual(response.status_code, 404)
    
class VoteTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_question_choice(self):
        question = Question.objects.create(question_text='What’s the weather like?', pub_date=timezone.now())
        question_choice = question.choice_set.create(choice_text='sunny')
        response = self.client.post(f'/polls/{question.id}/vote/', data={'choice':question_choice.id})
        modified_question = Question.objects.get(pk=question.id)
        voted_choice=modified_question.choice_set.get(pk=question_choice.id)
        self.assertEqual(question_choice.votes, 0)
        self.assertEqual(voted_choice.votes, 1)
        
        
       

    def test_post_redirects_to_results_page(self):
        question = Question.objects.create(question_text='Hello?', pub_date=timezone.now())
        question_choice = question.choice_set.create(choice_text='Yes')
        response = self.client.post(f'/polls/{question.id}/vote/', data={'choice':question_choice.id})
        self.assertRedirects(response, reverse('polls:results', args=[question.id]))