from django import forms
from .models import Article, Category, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('author', 'title', 'content', 'image', 'category', 'tag', 'pin')
        widgets = {
            'content': forms.Textarea(attrs={'class':'editable', 'placeholder':'Start Writing...' },),
            'title': forms.TextInput(attrs={'placeholder':'Insert Title here...'},)
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'class':'editable'})
        }