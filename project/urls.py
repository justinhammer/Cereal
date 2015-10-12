"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^cereal_list/$', 'main.views.cereal_list'),
    url(r'^cereal_detail/(?P<pk>\d+)/$', 'main.views.cereal_detail'),
    url(r'^cereal_search/$', 'main.views.cereal_search'),
    url(r'^manufacturer_detail/(?P<pk>\d+)/$', 'main.views.manufacturer_detail'),
    url(r'^create_view1/$', 'main.views.create_view1'),
    url(r'^create_view2/$', 'main.views.create_view2'),
    url(r'^update_view/(?P<pk>\d+)/$', 'main.views.update_view'),
]
