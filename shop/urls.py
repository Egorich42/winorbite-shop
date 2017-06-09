#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductList, name='ProductList'),
    url(r'^categorys/$', views.categoryList, name='categoryList'),
    url(r'^categorys/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ProductDetail, name='ProductDetail'),
    url(r'^about/contact/$', views.contactList, name='contactList'),
    url(r'^about/payment/$', views.paymentList, name='paymentList'),
]
