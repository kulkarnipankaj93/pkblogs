from django.contrib import admin
from .models import Post, Comment

# Register your models here.
#admin.site.register(Post)
#admin.site.register(Comment)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['title', 'slug', 'author', 'status'] # Add functionality to filter on admin page
    list_display = ['title', 'slug', 'author', 'status'] # display given fields on front page of admin
    search_fields = ['title', 'body'] # add search bar on admin page to search by 'title' and 'body'
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass