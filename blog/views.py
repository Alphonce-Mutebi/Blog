from django.shortcuts import render

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
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})

