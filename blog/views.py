from django.shortcuts import render , get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context  = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request):
    context = {'title' : 'BitCoin has been Fucked !' , 'content' : 'BitCoin price is now 000!' , 'author' : 'Mahdi Pashapur'}
    return render(request , 'blog/blog-single.html' , context)

# def test(request , name , family_name , age):
def test(request , pid):
    # posts = Post.objects.filter(status=1)
    # posts = Post.objects.all()
    # context  = {'posts' : posts}

    # context = {'name' : name , 'family_name' : family_name , 'age' : age}
    # context = {'pid' : pid}

    # post = Post.objects.get(id = pid)
    post = get_object_or_404(Post , pk=pid)
    context = {'post' : post}
    return render(request , 'test.html' , context)