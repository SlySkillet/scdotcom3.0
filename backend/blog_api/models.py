from django.db import models


class Tag(models.Model):
    theme = models.CharField(max_length=20)

    def __str__(self):
        return self.theme


class BlogPost(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
    image = models.ImageField(upload_to="images/", blank=True)
    image_caption = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="blog_posts", blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TechTag(models.Model):
    name = models.CharField(max_length=20)
    icon = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ScreenShot(models.Model):
    screenshot = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    published_date = models.DateTimeField(auto_now_add=False)
    last_updated = models.DateField(auto_now=True)
    title = models.CharField(max_length=200)
    tech_list = models.ManyToManyField(TechTag, related_name="projects", blank=True)
    primary_tech = models.ManyToManyField(
        TechTag, related_name="projects_primary", blank=True
    )
    screenshots = models.ManyToManyField(
        ScreenShot, related_name="project_images", blank=True
    )
    live_link = models.URLField(max_length=200, blank=True, null=True)
    repo_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
