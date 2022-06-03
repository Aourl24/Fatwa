from django.shortcuts import render, redirect
from .models import Question, Answer, Profile,Anon
from .form import QForm, AForm, PForm, UForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from django.db import ValueError
from django.contrib.auth.decorators import login_required
from .decorator import decorators
import time
from django.db.models import F
from notifications.signals import notify
from django.shortcuts import get_object_or_404
#from django.http import JsonRsponse

def fview(request):
#Home View, it display the question
    questions=Question()
    b=Question()
    answer=Answer()
    try:
        
        currentUser=Profile.objects.get(user__username=request.user)
        uquestion=questions.unactive_question(profile=currentUser)
    except ObjectDoesNotExist:
        uquestion=None

# uquestion was used to display pending questions on the html template    
# the try was used incase the user was not Log in, it should raise DoesNotExist error because of the user instance we create.So the try is to prevent this error   
        
    nanswer=answer.recently_add
    
    questions=questions.active_question
    
    nquestion=''
    pquestion=''
    mquestion=''
# mquestion and nquestion are set to '' to prevent us from getting Object refrence before assignment error
        
    if request.method=='POST':
        Filter=request.POST.get('filter')
        print(Filter)
        if Filter =='Most':
            
            mquestion=b.most_answer
        elif Filter == 'Recent':
            nquestion=b.recently_add
            
        elif Filter == 'Popular':
            pquestion=b.most_popular
       
        else:
            mquestion=None
            nquestion=None
            pquestion=None
                
    else:
        mquestion=None
        nquestion=None
        pquestion=None
        
    
        
    return render(request, 'home.html', {'questions':questions, 'uquestion':uquestion, 'mquestion':mquestion ,'pquestion':pquestion, 'nquestion':nquestion,'currentUser':currentUser})

# the prefix m-most, u-unactive, n-new questions   
@login_required(login_url='account_login')
def like2view(request,id):
    currentUser=Profile.objects.get(user__username=request.user)
    #id=request.GET.get('questionId')
    question=Question.objects.get(id=id)
    #check=Question.objects.filter(id=id, Support=currentUser).exists()
    check=Question.objects.filter(id=id, Support=currentUser).exists()
    if check:
        Question.objects.get(id=id).Support.remove(currentUser)
        return render(request, 'like2.html',{'question':question,'currentUser':currentUser})
    else:
        Question.objects.get(id=id).Support.add(currentUser)
        return render(request, 'like2.html',{'question':question, 'currentUser':currentUser})
        
    
        
        
       
           
    


@login_required(login_url='account_login')
#@decorators
def Qfview(request):
# the Ask Question view
    form=QForm(request.POST)
    if form.is_valid():
        try:
            currentUser=Profile.objects.get(user__username=request.user)
            formBody=form['body'].value()
            title=form['title'].value()
            if title is None:
                Question.objects.create(name=currentUser, body=formBody, active=False)
            else:
                Question.objects.create(name=currentUser, body=formBody, active=False, title=title)
            return redirect('/page/home')
        except ObjectDoesNotExist:
            #messages.error(request, 'Login to Ask a Question')
            return redirect('/login')
        
    return render(request, 'create.html', {'form':form})
        
      
def sview(request, id):
# show the detail view
    currentUser=Profile.objects.get(user__username=request.user)
    question=Question.objects.get(id=id)
    g=re
    question.Views=question.Views + 1
    question.save()
    #ses=Session.objects.get(session_key=request.session.session_key)
    ses=request.session.session_key
    #print( ses)
    #time.sleep(5)
    ans=Answer()
    #ans.likeCheck(currentUser)
    Ganswer=''
    answers=Answer.objects.filter(question=question, reply=None, active=True).order_by('-date')
        #question.question.like.add(g)
    form=AForm(use_required_attribute=False)
    Recipient=question.name
    try:
        if request.method=='POST':
            form=AForm(request.POST)
            if form.is_valid():
                
                print(Recipient)
                currentUser=Profile.objects.get(user__username=request.user)
                formBody=form['body'].value()
                j=request.POST.get('answer_id')
                #m=Answer.objects.get(id=j)
                Nuser= get_object_or_404(User, username=Recipient)
                print(j)
                co=None
                if j:
                    co=Answer.objects.get(id=j)
                    print(co)
                f=Answer.objects.create(body=formBody, user=currentUser, question=question, reply=co)
                f.save()
                notify.send(request.user,recipient=Nuser, verb='Someone Answer Your Question')
                
                return redirect(request.path_info)
            
           
        else:
            form=AForm()
                                    
                                                                                           
    except ObjectDoesNotExist:
            #messages.error(request, 'Login to Engage in Activities')
            return redirect('/login')
        
    return render(request, 'detail.html', {'question':question, 'form':form, 'answers':answers, 'currentUser':currentUser})
 
# j-to get the answer_id value from the detail template 
# co-after getting j, we get the Answer() which id is j 
# g- to get the like button value, but it was meant just to know whether the button is pressed and has nothing to do with the value
# p- same as g but was meant for the dislike button

@login_required(login_url='account_login')
def likeV(request, id):
    try: 
        currentUser=Profile.objects.get(user__username=request.user)
            #question=Question.objects.get(id=id)
            #answers=Answer.objects.filter(question=question, reply=None, active=True).order_by('-date')
            #answers=Answer.objects.filter(question=question, reply=None, active=True).order_by('-date')
        Recipient=request.GET.get('sender')
        g=request.GET.get('lieb')
        answer=Answer.objects.get(id=id)
    except:
        pass
        #p=request.GET.get('dislike')
    Nuser= get_object_or_404(User, username=Recipient)
    print(Nuser)
    print(Recipient)
    print(g)
        #currentUser=Profile.objects.get(user__username=request.user)
                
        #Janswer=Answer.objects.filter(question=question, id=g, like=currentUser).exists()
    Manswer=answer.like.filter(id=currentUser.id).exists()
    print(Manswer)
        #print(Janswer)      
                   
             #Lanswer=Answer.objects.filter(question=question, id=g, dislike=currentUser).exists()
                       
    if Manswer is True:
            #Banswer=Answer.objects.get(question=question, id=g).like.remove(currentUser)
        answer.like.remove(currentUser)
        answer.save()
        return render(request, 'like.html',{'currentUser':currentUser,'answer':answer})
    elif Manswer is False:
        answer.like.add(currentUser)
                 #Banswer=Answer.objects.get(question=question, id=g).like.add(currentUser)
        answer.save()
                
        notify.send(request.user, recipient=Nuser, verb='Someone Like Your Answer')
        return render(request, 'like.html',{'currentUser':currentUser,'answer':answer})
 
    #return render(request, 'like.html',{'question':question,'answer':answer, 'currentUser':currentUser})
 


@login_required(login_url='account_login') 
def pview(request):
    try:
        user=Profile.objects.get(user__username=request.user)
# the user get the request.user through the Profile models

        Quest=Question()
        answer=Answer()
        pquestion=Quest.user_question(profile=user)
# the user_question attribute is used to get the questions of the argument , the argument is user

        panswer=answer.user_answer(profile=user)
        form=UForm()
        if request.method=='POST':
            form=UForm(request.POST, instance=request.user)
# this form is UserChangeForm that is why it has an instance
            if form.is_valid():
                form.save()       
    except ObjectDoesNotExist :
        #messages.error(request, 'Kindly Login to View your Profile or SignUp to Create your Profile with us')
        return redirect('/login')
        
    
    return render(request, 'profile.html',{'pquestion':pquestion, 'panswer':panswer, 'form':form} )
    
    
def aview(request):
    
    return render(request, 'about.html')
    
def pendview(request):
    questions=Question()
    user=Profile.objects.get(user__username=request.user)
    uquestions=questions.unactive_question(profile=user)
    
    if request.method=='POST':
        gh=request.POST.get('pend')
        questions.delete_question(int(gh))
        
        
    return render(request, 'pend.html', {'uquestions':uquestions})
    
def landview(request):
    
    return render(request, 'landing.html')
    
    
def searchview(request):
    if request.method=='GET':
        try:
    
        
            text=request.GET.get('searchtext')
            stquestions=Question.objects.filter(title__icontains=text,active=True)
            squestions=Question.objects.filter(body__icontains=text, active=True)
            
        except ValueError:
            squestions=None
            stquestions=None
                
    else:
        squestions=Question()
        stquestions=Question()
    
    return render (request, 'search.html', {'squestions':squestions,'stquestions':stquestions})
    
def notificationview(request):
    #noti=Notification.object.unread()
    noti=request.user.notifications.unread()
    noti.mark_all_as_read()
    return render(request, 'notification.html')
    
def dark(request):
    if 'dark' in request.GET:
        b=request.GET.get('dark')
        ses=request.session.session_key
        print(ses)
        try:
            Mode=Profile.objects.get(user__username=request.user)
        except ObjectDoesNotExist:
                h='Unknown'
                #h=request.session.session_key
                #if Anon.objects.get(key=h).exists():
                
                Mode=Anon.objects.get(Key=h)
                
          
                
                
             
            
        j=Mode.mode
        if j == 'Light':
            Mode.mode='Dark'
            Mode.save()
            
           
        else:
            Mode.mode='Light'
            Mode.save()
            
      
      
      
    return redirect(b)
            
        
    
    