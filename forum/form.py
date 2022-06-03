from .models import Group, Post, Comment
from django import forms

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=['name']
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['body']
        
class CommentForm(forms.ModelForm):
    body=forms.CharField(label='', widget=forms.TextInput(attrs={'label':'', 'class':'textfieldR', 'placeholder':'Message'}))
    class Meta:
        model=Comment
        fields=['body']  