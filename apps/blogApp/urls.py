from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _
from django.urls import re_path

app_name = 'blogApp'


urlpatterns = [
    path('', views.PostList.as_view(), name='all_posts'),
    re_path(r'^category/(?P<category>[-\w]+)/$', views.CategoryListView.as_view(), name='category_list'),
    re_path(r'^(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post_detail'),
    path('search/keyword/', views.PostSearch.as_view(), name='search'),
]
