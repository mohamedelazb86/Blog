from django.urls import path
from .views import post_detail,postlist,create_post,update_post


urlpatterns = [
    path('',postlist),
    path('<int:id>',post_detail),
    path('create_post',create_post),
    path('update/<int:pk>',update_post),
]
