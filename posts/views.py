from django.shortcuts import render
from .models import Post,Comment,Category

def postlist(request):
    posts=Post.objects.all()
    context={
        'post_list':posts
    }
    return render(request,'posts/post_list.html',context)

def post_detail(request,id):
    post=Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'posts/post_detail.html',context)

