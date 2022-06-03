from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .models import Group
from ask.models import Profile

def decorators(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/login')
    return wrap


#def allow_role(*args):
#    def admin(view_func):
#        def wrap(request, *args, **kwargs):
#            if arg in 

def member(view_func):
    def wrap(request,*args,  **kwargs):
        user=Profile.objects.get(user__username=request.user)
        mem=Group()
                
        d=mem.GroupMemberId(id=kwargs['id'])
            
        if user in d():
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
            #return redirect('group')
    return wrap
    
       