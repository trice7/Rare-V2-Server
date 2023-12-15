from django.db import models 
from .user import User
from .post import Post

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
