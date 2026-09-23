from django.shortcuts import render
from blog.models import Post
# Create your views here.
def blog_view(request):
    return render(request , 'blog/blog-home.html')

def blog_single(request):
    context = {'title' : 'BitCoin has been Fucked !' , 'content' : 'BitCoin price is now 000!' , 'author' : 'Mahdi Pashapur'}
    return render(request , 'blog/blog-single.html' , context)

def test(request):
    # posts = Post.objects.filter(status=1)
    posts = Post.objects.all()
    context  = {'posts' : posts}
    return render(request , 'test.html' , context)