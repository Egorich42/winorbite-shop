#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import *
from django.http import HttpResponse

def show_data_list(request):
    datas = GObject.objects.all()
    datas_values = datas.values('location_y', 'location_x')

#    values = [f[key] for key in['location_y', 'location_x'] for f in datas_values]
#    values = [f[key]  for key in datas_values]
#    values = [f['location_x'] for f in datas_values]
#    values_y = [f['location_y'] for f in datas_values]
    return render(request, 'data/datalist.html', {'datas': datas })

