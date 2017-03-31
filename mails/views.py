#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from django import forms
from django.core.mail import *
import requests

# Create your views here.
def index(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('edit', pk=post.pk)
    else:
        form = MailForm()

    return render(request, 'blog/edit.html',{'form': form}) 
