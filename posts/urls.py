from django.urls import path
from .views import post_detail,postlist,create_post,update_post,delete_post
from .view2 import PostList,Post_Detail,Create_Post,Update_post,Delete_pos


urlpatterns = [
    path('',postlist),
    path('<int:id>',post_detail),
    path('create_post',create_post),
    path('update/<int:pk>',update_post),
    path('delete/<int:pk>',delete_post),

    # path for crd by cbv
    path('posts',PostList.as_view()),
    path('delete/<int:pk>',Delete_pos.as_view()),
    path('posts/create',Create_Post.as_view()),
    path('posts/update/<int:pk>',Update_post.as_view()),
    path('posts/delete/<int:pk>',Delete_pos.as_view())
]
