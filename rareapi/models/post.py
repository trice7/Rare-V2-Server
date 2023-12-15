from django.db import models
from .category import Category
from .user import User

class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField(auto_now_add=True)
  image_url = models.CharField(max_length=50)
  content = models.TextField()
  approved = models.BooleanField()
