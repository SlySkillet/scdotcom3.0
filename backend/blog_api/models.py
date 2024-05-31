from django.db import models

# Create your models here.
class BlogPost(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
