from django.shortcuts import render, get_object_or_404
from blogentries_app.models import Post
# Create your views here.



def blogentries(request):

    post = Post.objects.all()

    context = {
        'post' : post
    }

    return render(request, 'blogentries/blog.html', context)

def detail(request, pk):

    post = get_object_or_404(Post, id=pk)

    context = {
        'post' : post
    }
    return render(request, 'blogentries/post-details.html', context)