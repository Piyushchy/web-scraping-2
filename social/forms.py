from django import forms
from .models import Post, Comment
class PostForm(forms.ModelForm):
    body = forms.body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder':'What are you thinking?', 'style':'padding: 10px;'}), label='') 
    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='')
    class Meta:
        model = Comment
        fields = ['comment']