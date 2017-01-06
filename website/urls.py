from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^srk/$', include(admin.site.urls)),
    url(r'^', include('personal.urls')),
)
