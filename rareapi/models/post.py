from django.db import models

class Post(models.Model):
  rare_user = models.CharField(max_length=50)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  publication_date = models.DateField(auto_now_add=True)
  image_url = models.CharField(max_length=50)
  content = models.TextField()
  approved = models.BooleanField()
