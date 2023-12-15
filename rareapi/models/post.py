from django.db import models
from rareapi.models import rare_user, Category

class Post(models.Model):
  rare_user = models.ForeignKey(rare_user, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField(auto_now_add=True)
  image_url = models.CharField(max_length=50)
  content = models.TextField()
  approved = models.BooleanField()
