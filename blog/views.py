from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# def posts(req):
#     posts = Post.objects.all()    
#     return render(req,'blog/posts.html',{"posts":posts})

def posts(req):
    all_posts = Post.objects.all().order_by("-created_at")
    paginator = Paginator(all_posts,6)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(req,'blog/posts.html',{"page_obj":page_obj})


def post_details(req,pk):
    post = Post.objects.get(id = pk)
    comments = post.comments.all().order_by("-created_at")
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = req.user
            comment.save()
            return redirect("post_details",pk=post.id)
    else: 
        form = CommentForm()
    return render(req,"blog/post_details.html",{"post":post,"form":form,"comments":comments})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("posts")
    else:
        form = PostForm()
    return render(request,'blog/create_post.html',{"form":form})

@login_required
def delete_post(req,pk):
    post = Post.objects.get(id = pk)
    if req.user == post.author:
        post.delete()
    return redirect("posts")
    