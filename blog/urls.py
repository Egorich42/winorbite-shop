#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^blog/$', views.PostList, name='PostList'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.PostDetail, name='PostDetail'),
]
