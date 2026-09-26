from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.db.models import F
# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(
        status=1,
        published_date__lte=timezone.now()
    )
    context  = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)

def blog_single(request,pid):
    post = get_object_or_404(Post , pk=pid)
    
    # increment the counted_view
    post.counted_view = F('counted_view') + 1
    post.save(update_fields=['counted_view'])

    # give the current counter from the DB after update
    post.refresh_from_db()
    context = {'post' : post}
    # context = {'title' : 'BitCoin has been Fucked !' , 'content' : 'BitCoin price is now 000!' , 'author' : 'Mahdi Pashapur'}
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

    # increment the counted_view
    post.counted_view = F('counted_view') + 1
    post.save(update_fields=['counted_view'])

    # give the current counter from the DB after update
    post.refresh_from_db()
    context = {'post' : post}
    return render(request , 'test.html' , context)