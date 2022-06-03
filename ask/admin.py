from django.contrib import admin
from django.contrib.auth.models import User
from ask.models import Question, Answer , Profile,Anon
from forum.models import Post, Comment
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display=['body', 'active']

admin.site.register(Profile)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
# Register your models here.

admin.site.register(Anon)
