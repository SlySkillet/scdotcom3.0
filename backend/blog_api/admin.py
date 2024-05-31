from django.contrib import admin
from .models import BlogPost, Tag

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on',)
    search_fields = ('title', 'tags__theme',)
    list_filter = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ('theme',)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag, TagAdmin)
