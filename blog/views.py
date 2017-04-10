#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import *
from django.http import HttpResponse
from .forms import *

def create_post(request):
    if request.method == "POST":
        form = write_post(request.POST)  
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog/post_detail.html', pk=post.pk)
    else:
        form = write_post()

    return render(request, 'blog/edit.html',{'form': form}) 



def full_post(request):
	


def post_list(request):
    posts = Post.objects.all().order_by('created')
    return render(request, 'blog/postlist.html', {'posts': posts })




