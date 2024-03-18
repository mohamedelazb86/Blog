from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):

    title=models.CharField(max_length=100)
    user=models.ForeignKey( User,related_name='post_user',on_delete=models.SET_NULL,null=True,blank=True)
    content=models.TextField(max_length=1500)
    draft=models.BooleanField(default=True)
    publish_date=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey('Category',related_name='post_category',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_post')
    tags = TaggableManager()

    def __str__(self):
        return self.title




class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Comment(models.Model):

    user=models.CharField(max_length=120)
    content=models.TextField(max_length=250)
    publish_date=models.DateTimeField(default=timezone.now)
    post=models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


