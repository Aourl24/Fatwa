from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied


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

def member_only(**kwargs):
    def member(view_function):
        def wrap(request, *args, **kwargs):
            if request.user in kwargs:
                return view_function(request, **args, **kwargs)
            else:
                return  PermissionDenied
        return wrap
    return member
       