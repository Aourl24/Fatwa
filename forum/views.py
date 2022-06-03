from django.shortcuts import render, redirect
from .models import Post, Comment, Group
from .form import GroupForm, PostForm, CommentForm
from ask.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from .decorator import member
from  notifications.signals import notify
from django.contrib.auth.models import User

def GroupView(request):
    mygroup=Group()
    groups=mygroup.excludeGroup(request.user)
    mygroups=mygroup.getGroup(request.user)
    #groups=Group.objects.all()
    return render(request, 'forumt/group.html', {'groups':groups, 'mygroups':mygroups})
    
    
    
    
def Postview(request):
    posts=Post.objects.all()
    a='forumt/fhome.html'
    return render(request ,a,  {'posts':posts})

def CreatePost(request):
    form=PostForm()
    user=Profile.objects.get(user__username=request.user)
    if request.method=='GET':
        groupname=request.GET.get('groupname')
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            groupnam=request.GET.get('groupname')
            id=request.GET.get('id')
            
            
            try:
                GroupName=Group.objects.get(name=groupnam)
                
                a=form.save(commit=False)
                a.name=user
                a.group=GroupName
                a.save()
            except ObjectDoesNotExist:
                pass
            
            #return redirect ('http:/for/group' +id)
            return redirect('groupdetail', id=id)
            
    return render(request, 'forumt/CF.html', {'form':form})
    
    
    
def detailview(request, id):
    post=Post.objects.get(id=id)
    return render(request, 'forumt/fdetail.html', {'post':post})      

def GroupFormView(request):
    form=GroupForm()
    if request.method=='POST':
        form=GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group') 
            
    return render(request, 'forumt/GFV.html', {'form':form}) 

@member
def GroupInfo(request, id):
    group=Group.objects.get(id=id)
    
    
    post=Post()
    posts=post.GroupPost(group)

    
    
    return render(request, 'forumt/groupInfo.html', {'group':group, 'posts':posts})
    
def joinGroup(request):
    group=Group()
    
    groups=group.joinGroup('', '')
    
    return render(request, 'JoinG.html')
    
def Pactivity(request, id):
    activity=Post.objects.get(id=id)
    Curruser=Profile.objects.get(user__username=request.user)
    form=CommentForm()
    comment=Comment()
    comments=comment.PostComment(activity)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            #postId=request.GET.get('PostId')
            #c=Post.objects.get(id=id)
            Pform=form.save(commit=False)
            Pform.name=Curruser
            Pform.post=activity
            #Pform.reply=None
            Pform.save()
            return redirect(request.path_info)
        
    
    return render(request, 'forumt/Postact.html', {'activity':activity, 'form':form, 'comments':comments, 'Curruser':Curruser})
    
def joinGroup(request):
    user=Profile.objects.get(user__username=request.user)
    group=Group()
    if request.method=='GET':
        l=request.GET.get('join')
        u=request.GET.get('admin')
        if l:
            Nuser=User.objects.get(username=u)
            notify.send(request.user, recipient=Nuser, verb=('{} Request to join Your Community').format(request.user))
            confirm=group.JoinGroup(l, user)
        #return confirm
        
    return render(request, 'forumt/JoinCom.html')

def AdminView(request):
    group=Group()
    user=Profile.objects.get(user__username=request.user)
    
    #join=group.JoinGroup('', '')
    #remove=group.RemoveMember('', '')
    acts=''
    if 'Groupname' in request.GET:
        
        name=request.GET.get('Groupname')
        print(name)
        if name:
            acts=Group.objects.filter(admin=user, name=name).all()
        else:
            acts=''
    
            
    
    return render(request, 'forumt/adminG.html', {'acts':acts})
               