from django.test import TestCase
from django.contrib.auth.models import User
from ask.models import Question, Answer 
from datetime import datetime

class QTest(TestCase):
    #a=User.objects.create(username='awwal')
    
    date=datetime.now()
    body='Good to be here'
    active=True
    
    
    def firsttest(self):
        a=User.objects.create(username='Yusuf')
        b=Question.objects.create(user=a, date=datetime.now(), body='hw are you', active=True)
        return b
        
    def secondtest(self):
        #a=User.objects.create(username='Awwal')
        j=self.firsttest()
        s=User.objects.create(username='Malik')
        #b=Question.objects.create(user=a, date=datetime.now(), body='hw are you', active=True)
        e=Answer.objects.create(question=j, user=s, body='hello', date=datetime.now, active=True)
        return e
        #=self.firsttest()
        
         
           
    def testpage(self):
        #d=self.firsttest()
        f=self.secondtest()
        #self.assertTrue(isinstance(d, Question))
        self.assertTrue(isinstance(f, Answer))
    