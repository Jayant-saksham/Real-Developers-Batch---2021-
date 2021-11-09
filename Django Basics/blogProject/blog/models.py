from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    user = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = "Aricle/Image/")
    content = models.TextField()
    