#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.create_post, name='create_post'),
]
=======
    url(r'^create/$', views.create_post, name='create_post'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
]
>>>>>>> 37507b5fd550b7e13e4051ab5f5864867e99b54e
