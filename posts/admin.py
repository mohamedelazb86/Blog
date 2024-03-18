from django.contrib import admin
from .models import Post,Comment,Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.




class PostAmin(SummernoteModelAdmin):
    list_display=['title','publish_date','draft']
    list_filter=['draft']
    search_fields=['title']

    summernote_fields = ('content',)

admin.site.register(Post,PostAmin)
admin.site.register(Category)
admin.site.register(Comment)


