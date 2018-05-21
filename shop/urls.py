#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from blog import views as b_views
from django.http import HttpResponse
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', b_views.post_list, name='post_list'),
    url(r'^shop/$', views.categoryList, name='categoryList'),
    url(r'^shop/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^about/contact/$', views.contactList, name='contactList'),
    url(r'^about/payment/$', views.paymentList, name='paymentList'),
    url(r'^about/privacy/$', views.privacy, name='privacy'),
]
