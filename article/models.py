from django.db import models


# Create your models here.
class Article(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    keyset = models.TextField(default='')
    created_at = models.DateField(auto_now_add=True)
