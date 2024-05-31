from django.db import models

# Create your models here.
class Tag(models.Model):
    theme = models.CharField(max_length=20)

    def __str__(self):
        return self.theme


class BlogPost(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
    image = models.ImageField(upload_to='images/', blank=True)
    image_caption = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True)

    def __str__(self):
        return self.title
