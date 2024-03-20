from .models import Post
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import PostListSerializers,Post_DetailSerializers


class PostlistApi(ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListSerializers

class Post_DetailApi(RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_DetailSerializers