from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #blogs urls
    url(r'^$', 'blogs.views.home'),


]
