from django.contrib import admin
from .models import Post, Comment, UserProfile,Game
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Game)
# Register your models here.
