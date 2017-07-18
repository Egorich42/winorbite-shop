#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^shop/$', views.categoryList, name='categoryList'),
    url(r'^shop/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^about/contact/$', views.contactList, name='contactList'),
    url(r'^about/payment/$', views.paymentList, name='paymentList'),
    url(r'^about/privacy/$', views.privacy, name='privacy'),
]
