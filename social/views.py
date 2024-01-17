from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class PostListView(LoginRequiredMixin,View):
    def get (self,request,*args,**kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        context = {
            'posts':posts,
            'form':form ,
        }
        return render(request,'social/index.html',context)
    def post(self,request,*args,**kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        context = {
            'posts':posts,
            'form':form ,
        }
        return render(request,'social/index.html',context)
# Create your views here.
class PostDetailView(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post':post,
            'form':form,
            'comments':comments,
        }
    
        return render(request,'social/post_detail.html',context)
    def post(self,request,pk,*args,**kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        print("here")
        if form.is_valid():
  
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
        comments = Comment.objects.filter(post=post).order_by('-created_on')
        context = {
            'post':post,
            'form':form,
            'comments':comments,
        }
    
        return render(request,'social/post_detail.html',context)
class PostEditView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['body']
    template_name = 'social/post_edit.html'
    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.pk})
    def test_func(self) :
        post = self.get_object()
        return self.request.user == post.author
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'social/post_delete.html'
    success_url = reverse_lazy('post-list')
    def test_func(self) :
        post = self.get_object()
        return self.request.user == post.author
class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  
    model = Comment
    template_name = 'social/comment_delete.html'
    def get_success_url(self):
        return reverse_lazy('post-detail',kwargs={'pk':self.object.post.pk})
    def test_func(self) :
        print("here")
   
        comment = self.get_object()
        return self.request.user == comment.author