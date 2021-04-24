from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views, sitemaps

app_name = 'baseApp'

sitemaps_dict = {'Static_sitemap': sitemaps.StaticSitemap,
                'Project_sitemap': sitemaps.ProjectSitemap,
                'AllPosts_sitemap': sitemaps.AllPostSitemap,
                'PostCategories_sitemap': sitemaps.PostCategoriesSitemap_en,
                'Post_sitemap': sitemaps.PostSitemap_en,
                }

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>', views.ProjectDetailView.as_view(), name='project_detail'),

    # This is for sitemap.xml
    path('LavinoMap.xml', sitemap, {'sitemaps': sitemaps_dict},
     name='django.contrib.sitemaps.views.sitemap'),
]
#
#
# handler404 = 'apps.baseApp.views.error_404'
# handler500 = 'apps.baseApp.views.error_500'
