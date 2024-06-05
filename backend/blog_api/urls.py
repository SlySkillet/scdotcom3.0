from django.urls import path
from .views import ListBlogPosts, BlogPostDetail


urlpatterns = [
    path("blogposts/", ListBlogPosts.as_view(), name="blog-posts"),
    path("blogposts/<int:pk>/", BlogPostDetail.as_view(), name="blog-post-detail")
]
