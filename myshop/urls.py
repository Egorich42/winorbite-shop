#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^order/', include('orders.urls', namespace='orders')),
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
 #   url(r'^CMR/', include('CMR.urls', namespace='CMR')),
#    url(r'^data/', include('data.urls', namespace='data')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
