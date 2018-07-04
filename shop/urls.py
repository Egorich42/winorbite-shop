#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from blog import views as b_views
from django.http import HttpResponse
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', b_views.post_list, name='post_list'),
]
