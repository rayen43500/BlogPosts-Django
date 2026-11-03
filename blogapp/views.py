from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Author, BlogPost


class BlogView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'Posts/blogView.html'


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author']
    template_name = 'Posts/blogcreate.html'
    success_url = reverse_lazy('Posts:listhtml')


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'author']
    template_name = 'Posts/blogUpdate.html'
    success_url = reverse_lazy('Posts:listhtml')


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = 'Posts/blogdelete.html'
    success_url = reverse_lazy('Posts:listhtml')


class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'Posts/authorList.html'


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'email', 'bio']
    template_name = 'Posts/authorForm.html'
    success_url = reverse_lazy('Posts:authors')
