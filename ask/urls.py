from django.contrib import admin
from django.urls import path
from .views import fview, Qfview, sview, pview,aview, pendview, searchview, notificationview,dark,likeV, like2view


urlpatterns=[
    path('home/', fview, name='home'),
    path('create/', Qfview, name= 'create'),
    path('Q<int:id>/', sview,  name='detail'), 
    path('like<int:id>/', likeV, name='lyk'),
    path('profile/', pview, name='profile'), 
    path('about/', aview, name='about'), 
    path('pend/', pendview, name='pend'), 
    path('search/', searchview, name='search'),    
    path('notify/', notificationview, name='notify'),
    path('dark/', dark, name='darkmode'),
    path('<int:id>/', like2view, name='like'),
]