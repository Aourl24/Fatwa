from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
from datetime import datetime,date, timedelta
from django.db.models import Count   
from django.db import models
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
#from django.utils.encoding import python_2_unicode_compatible


check=(('A',  'Islam By Birth'),
        ('B', 'Convert'),
        ('C','Other') )

basic=(('A',  'Basic'),
        ('B', 'Intermediary'),
        ('C','Advanced') )
        
last=(('A',  'Prophet Isa'),
        ('B', 'Prophet Musa'),
        ('C','Prophet Muhammed'),
        ('D','Prophet Ibrahim') )
                               
color=(('Light',  'Light'),
        ('Dark', 'Dark'), )

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='ProfUser')
    follow=models.ManyToManyField('self', related_name='follows', symmetrical=False)
    age=models.DateField(null=True,blank=True)
    islam=models.CharField(max_length=100, choices=check, null=True)
    Basic_Knowledge=models.CharField(max_length=50, choices=basic, null=True, blank=True)
    NameofLastProphet=models.CharField(max_length=50,choices=last,null=True, blank=True)
    mode=models.CharField(max_length=10,choices=color, default='Light')
    
    
    
    def __str__(self):
        return self.user.username
    
    
class Question(models.Model):
    name=models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,  related_name='User')
    date=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=200, blank=True,null=True)
    body=models.CharField(max_length=1000)
    active=models.BooleanField(default=True)
    Support=models.ManyToManyField(Profile, related_name='support', blank=True, symmetrical=False)
    view=GenericRelation(HitCount, object_id_field='object_pk', related_name='countViews')
    Views=models.IntegerField(default=0, blank=True, null=True)
    
    
    
    def __str__(self):
        if self.title != None:
            return self.title
        else:
            return self.body
    
    def recently_add(self):
        recent=datetime.now()-timedelta(1)
        return Question.objects.filter(active=True).order_by('-date')
        
        
    def active_question(self):
        return Question.objects.filter(active=True)
        
    def unactive_question(self, profile):
        return Question.objects.filter(active=False, name=profile)
        
    def delete_question(self, question):
        return Question.objects.get(id=question).delete()

    def most_answer(self):
        return Question.objects.annotate(a=Count('question')).filter(active=True).order_by('-a')
        
    def user_question(self, profile):
        return Question.objects.filter(name=profile, active=True)
     
    def most_popular(self):
        return Question.objects.filter(active=True).order_by('-Views')       
    #class Meta:
#        ordering=['-date']
        
class Answer(models.Model):
    question=models.ForeignKey(Question, related_name='question', null=True, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='userName', null=True)
    date=models.DateTimeField(auto_now_add=True)
    body=models.CharField(max_length=1000)
    like=models.ManyToManyField(Profile, symmetrical=False, related_name='like', blank=True)
    dislike=models.ManyToManyField(Profile, symmetrical=False, related_name='dislike', blank=True)
    color=models.CharField(max_length=20, blank=True, null=True)
    
    reply=models.ForeignKey('self', related_name='replys', null=True, on_delete=models.CASCADE, blank=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        #currentUser=Profile.objects.get(user__username=user)
        
        
        return self.body
    
    
    def recently_add(self):
        recent=datetime.now()-timedelta(1)
        return Answer.objects.filter(date=datetime.now())[0:2]
        
        
    def active_Answer(self):
        return Answer.objects.filter(active=True)
        
    def most_like(self):
        return Question.objects.order_by(like)
    
    def user_answer(self, profile):
        return Answer.objects.filter(user=profile)[:5]
    
    def likeCheck(self, user):
        if user in self.like:
            return self.color=='Red'
        else:
            return self.color=='blue'
               
    def likeColor(self, id, Color):
        #check=Answer.objects.filter(question=question, id=g, dislike=currentUser).exists()
        return Answer.objects.filter(id=id).update(color=Color)
        
        
    class Meta:
        ordering=['-date']

       

class Anon(models.Model):
    Key=models.CharField(max_length=1000)
    mode=models.CharField(max_length=10,choices=color,default='Light')
    
    def __str__(self):
        return self.Key
            

#        newprofile.follow.set([instance.Profile.id])
#        newprofile.save()
#        
#post_save.connect(Creation, User)

    
    