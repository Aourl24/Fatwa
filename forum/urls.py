"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from forum.views import Postview, detailview, GroupView, GroupFormView, GroupInfo,Pactivity, AdminView,  CreatePost, joinGroup
from django.conf.urls.static import static
from django.conf import settings



    
urlpatterns = [
    path('home/', Postview, name='home2'), 
    path('<int:id>/', detailview, name='detailv') ,    
    path('Group/', GroupView, name='group'),
    path('GroupCreation', GroupFormView, name='groupform'), 
    path('group<int:id>/', GroupInfo, name='groupdetail'), 
    path('create/', CreatePost, name='createPost'), 
    path('A<int:id>/', Pactivity, name='activity'),
    path('Waiting/', joinGroup,  name='join'), 
    path('GroupAdmin/', AdminView, name='AdminG'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)