from django.db import models
from rareapi.models import Post, Tag

class PostTag(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)