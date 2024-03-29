"""personalWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

from django.urls import path, include

from .sitemaps import HomeSitemap, CategorySitemap, PostSitemap, ContactSitemap

from base.views import robots_txt, favicon_file, web_manifest_files

from django.conf import settings
from django.conf.urls.static import static

sitemaps = {'home': HomeSitemap, 'category': CategorySitemap, 'post': PostSitemap, 'contact': ContactSitemap,}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path("android-chrome-192x192.png", favicon_file),
    path("android-chrome-512x512.png", favicon_file),
    path("apple-touch-icon.png", favicon_file),
    path("browserconfig.xml", web_manifest_files),
    path("favicon-16x16.png", favicon_file),
    path("favicon-32x32.png", favicon_file),
    path("favicon.ico", favicon_file),
    path("mstile-150x150.png", favicon_file),
    path("safari-pinned-tab.svg", favicon_file),
    path("site.webmanifest", web_manifest_files),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('', include('base.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
