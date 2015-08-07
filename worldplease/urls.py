from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #blogs urls
    url(r'^$', 'blogs.views.home'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', 'blogs.views.detail'),
    #url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)$', 'blogs.views.detail'),


]
