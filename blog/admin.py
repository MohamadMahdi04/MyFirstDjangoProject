from django.contrib import admin
from blog.models import Post
# Register your models here.

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'createded_date'
    empty_value_display = '-empty-'
    list_display = ('title' , 'counted_view' , 'author' , 'status' , 'published_date' , 'createded_date' ,)
    list_filter = ['status' , 'author']
    ordering = ['-createded_date' ]
    search_fields = ['title' , 'content']
admin.site.register(Post , PostAdmin)