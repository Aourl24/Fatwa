from django.db import models
#from django.urls import reverse
from ask.models import Profile
from datetime import datetime

cat=(('Hadith', 'Hadith'), ('Fiqh','Fiqh') , ('Taoheed','Taoheed'), ('Language','Language'), ('General', 'General') )


class Group(models.Model):
    name=models.CharField(max_length=25)
    admin=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='admin', null=True)
    #announcement=models.ForeignKey(Post, related_name='announce', on_delete=models.CASCADE)
    member=models.ManyToManyField(Profile, related_name='group', symmetrical=False)
    
    
    #def __str__(self):
    #    return 'The {} Group'.format(self.name)
    def __str__(self):
        return self.name
        
    def getGroup(self, user):
        return Group.objects.filter(member__user__username=user).all()
        
    def GroupMember(self, GroupName):
        return Group.objects.get(name=GroupName).member.all()
        
    def excludeGroup(self, user):
        b=Group.objects.exclude(member__user__username=user).all()
        return b
    
    def GroupMemberId(self, id):
        return Group.objects.get(id=id).member.all
        
    def JoinGroup(self, GroupName, *user):
        for a in user:
            return Group.objects.get(name=GroupName).member.add(a)
        
    def RemoveMember(self, GroupName, *user):
        for a in user:
            return Group.objects.get(name=GroupName).member.remove(user)
            
    #def GroupPost(self, Group):
            

#class Membership(models.Model):
#    member_name=models.ForeignKey(Profile, related_name='')
#    group_name=models.ForeignKey(Group)          
    
class Post(models.Model):
    name=models.ForeignKey(Profile, related_name='puser', on_delete=models.CASCADE)
    group=models.ForeignKey(Group, related_name='PGroup', null=True, on_delete=models.CASCADE)
    #category=models.CharField(max_length=30, choices=cat)
    Date=models.DateTimeField(default=datetime.now())
    head=models.CharField(max_length=30)
    Image=models.ImageField(null=True, blank=True, upload_to='images/')
    body=models.TextField()
    
    
    def __str__(self):
        if self.head:
            return self.head
        else:
            return self.body    
    
    def GroupPost(self, GroupName):
        return Post.objects.filter(group__name=GroupName).all()
        #return Group.objects.filter(name=Group).member.puser.all()
        
        
        
    class Meta: 
        ordering = ['Date']
                        
class Comment(models.Model):
    post=models.ForeignKey(Post,    related_name='comment', on_delete=models.CASCADE)
    Date=models.DateTimeField(default=datetime.now())
    name=models.ForeignKey(Profile, null=True, blank=True,related_name='Cuser', on_delete=models.CASCADE) 
    body=models.TextField()
    reply=models.ForeignKey('self', related_name='replys', null=True, blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.body
        
    def PostComment(self, Post):
        return Comment.objects.filter(post=Post).all()
        
        
    class Meta:
        ordering=['Date']
    

