from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, DetailView, AuthorView, CreateView, NotFoundView
from users.views import LoginView, LogoutView
#from django.http import HttpResponseNotFound


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #blogs urls
    url(r'^$', HomeView.as_view(), name='blog_home'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)$', AuthorView.as_view(), name='blog_owner'),
    url(r'^blogs/_new$', CreateView.as_view(), name='blog_create'),

    # Users urls
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),

    #when other (error 404)
    url(r'^.*$', NotFoundView.as_view(), name='not_found_404'),
]
