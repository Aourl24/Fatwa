from django.test import TestCase
from django.contrib.auth.models import User
from ask.models import Question, Answer ,Profile
from datetime import datetime

# Create your tests here.
class QTest(TestCase):
    #a=User.objects.create(username='awwal')
    
    date=datetime.now()
    body='Good to be here'
    active=True
    
    
    def firsttest(self):
        a=Profile.objects.get(user__username='Bilal')
        b=Question.objects.create(name=a, date=datetime.now(), body='hw are you', active=True)
        return b
        
    def secondtest(self):
        #a=User.objects.create(username='Awwal')
        j=QTest.firsttest(self)
        s=Profile.objects.get(user__first_name='Bilal')
        #b=Question.objects.create(user=a, date=datetime.now(), body='hw are you', active=True)
        e=Answer.objects.create(question=j, user=s, body='hello', date=datetime.now, active=True)
        return e
        #=self.firsttest()
        
    #def testpage(self):
#        #d=self.firsttest()
#        f=QTest.secondtest(self)
#        #self.assertTrue(isinstance(d, Question))
#        self.assertTrue(isinstance(f, Answer))


class STest(TestCase):

    def test_details(self):

        response = self.client.get('/page/home/')

        self.assertEqual(response.status_code, 200)


    def test_index(self):

        response = self.client.get('/page/profile/')

        self.assertEqual(response.status_code, 200)
 