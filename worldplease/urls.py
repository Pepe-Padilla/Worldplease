from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #blogs urls
    url(r'^$', 'blogs.views.home', name='blog_home'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', 'blogs.views.detail', name='blog_detail'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)$', 'blogs.views.author', name='blog_owner' ),


    #when other (error 404)
    #url(r'^.*$', '')
]
