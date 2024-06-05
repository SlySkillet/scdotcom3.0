from django.urls import path
from .views import ListBlogPosts


urlpatterns = [
    path("blogposts/", ListBlogPosts.as_view(), name="blog-posts")
]
