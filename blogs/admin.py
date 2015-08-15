from django.contrib import admin
from blogs.models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'owner', 'status')
    list_filter = ('status',)
    search_fields = ('id', 'title')


admin.site.register(Blog, BlogAdmin)