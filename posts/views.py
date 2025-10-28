from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Status
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class PostListView(ListView):
    """
    PostListView is going to retrive all of the objects formt the Post table in the data base.
    """
    template_name = "posts/list.html"
    #model = Post
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numbers = [1,2,3,4,5,6]
        flag = True
        context["numbers"] = numbers
        context["flag"] = flag
        print(context)
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    """
    PostDetailView class is going to retrieve a single element from the post table in the data base.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "detailed"

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    PostCreateView class is going to let us make a new post.
    """
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    PostUpdateView class will allow us to update a current post.
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    PostDeleteView class will allow us to delete a post from the data base.
    """
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("posts_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            return self.request.user == post.author