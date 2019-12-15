from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

posts = [
    {
        'author' : 'CoreyMS',
        'content':'Blog Post 1',
        'title':'First Post Content',
        'date_posted':'August 27, 2018'
    },
    {
        'author' : 'Jane Doe',
        'content':'Blog Post 2',
        'title':'Second Post Content',
        'date_posted':'August 28, 2018'
    },

]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

