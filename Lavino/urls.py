"""Lavino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static


urlpatterns = [
    # path('robots.txt', include('robots.urls')),
    path('AdminPage/', admin.site.urls),
    # This is for Blog Editor in blogApp.models.py
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt', include('robots.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include('apps.baseApp.urls')),
    path('blog/', include('apps.blogApp.urls')),

    # prefix_default_language=False,
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
