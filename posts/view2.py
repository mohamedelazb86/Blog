from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView

# create crd operations

class PostList(ListView):
    
        model=Post
        template_name='posts/post_list.html'
        
        

class Post_Detail(DetailView):
   
        model=Post
        template_name='posts/post_detail.jtml'

class Create_Post(CreateView):
    
        model=Post
        fields='__all__'
        success_url='/posts/'
        template_name='posts/create_post.html'

class Update_post(UpdateView):
        model=Post
        fields='__all__'
        success_url='/posts/'
        template_name='posts/update.html'

class Delete_pos(DeleteView):
        model=Post
        success_url='/posts/'
        template_name='posts/delete_post.html'








