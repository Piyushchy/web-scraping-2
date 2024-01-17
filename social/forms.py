from django import forms
from .models import Post, Comment
class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'What are you thinking?'}),label='') 
    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Add a comment'}),label='')
    class Meta:
        model = Comment
        fields = ['comment']