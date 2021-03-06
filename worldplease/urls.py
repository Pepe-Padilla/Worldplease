from django.conf.urls import include, url
from django.contrib import admin
from blogs.views import HomeView, DetailView, AuthorView, CreateView, NotFoundView, MyBlogView, EditView
from users.views import LoginView, LogoutView, bloguersView, SignupView
from blogs.api import BlogListAPI, BlogDetailAPI
from users.api import UserDetailAPI, UserListlAPI
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #blogs urls
    url(r'^$', HomeView.as_view(), name='blog_home'),
    url(r'^blogs/edit/(?P<ownerName>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', login_required(EditView.as_view()), name='blog_edit'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)/(?P<pk>[0-9]+)$', DetailView.as_view(), name='blog_detail'),
    url(r'^blogs/(?P<ownerName>[a-zA-Z0-9]+)$', AuthorView.as_view(), name='blog_owner'),
    url(r'^blogs/_new$', login_required(CreateView.as_view()), name='blog_create'),
    url(r'^blogs/_myBlogs$', login_required(MyBlogView.as_view()), name='blog_my'),

    # Users urls
    url(r'^blogs$', bloguersView.as_view(), name='blogers_list'),
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^singup$', SignupView.as_view(), name='users_singup'),

    # Blogs API URLs
    url(r'^api/1.0/blogs$', BlogListAPI.as_view(), name='blog_list_api'),
    url(r'^api/1.0/blogs/(?P<pk>[0-9]+)$', BlogDetailAPI.as_view(), name='blog_detail_api'),

    # Users API URLs
    url(r'^api/1.0/users$', UserListlAPI.as_view(), name='users_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='users_detail_api'),

    #when other (error 404)
    url(r'^.*$', NotFoundView.as_view(), name='not_found_404'),
]

