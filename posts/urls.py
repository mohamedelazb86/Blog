from django.urls import path
from .views import post_detail,postlist


urlpatterns = [
    path('',postlist),
    path('<int:id>',post_detail),
]
