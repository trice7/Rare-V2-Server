from django.db import models 
from .rare_user import rare_user

class Comment(models.Model):
    author_id = models.ForeignKey(rare_user, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_on = models.DateTimeField()