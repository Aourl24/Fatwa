from .models import Question, Answer, Profile
from django import forms
from django.contrib.auth.models import User
class QForm (forms.ModelForm):
    title=forms.CharField(label='Title(optional)',required=None, widget=forms.TextInput(attrs={'style':'margin:4px;', 'class':'Qinput'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Ask a Question', 'class':'text', 'style':'margin:4px;'}))
    class Meta:
        model=Question
        fields=['title', 'body']
        require=None
        
class AForm(forms.ModelForm):
    body=forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Input Text', 'class':'forminput'}))
    
    class Meta:
        model=Answer
        fields=['body']
        #use_required_attribute=False
        
class PForm(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['age' , 'islam']   

class UForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name']      