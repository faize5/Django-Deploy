from multiprocessing.reduction import register
from .models import Comment, Post
from django.contrib import admin
from blog.models import UserProfileInfo


admin.site.register(UserProfileInfo)
admin.site.register(Post)
admin.site.register(Comment)