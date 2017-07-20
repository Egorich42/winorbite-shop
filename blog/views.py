#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django import forms
import requests
 
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
  #          link = blog_link+'why-sovki-hate-superman'
            link = blog_link+post.slug
            vk_text = post.text_to_vk
            vk_api.wall.post(owner_id=-140316393,attachments=alpha, message=vk_text,from_group=1,signed=1) 
            return render(request, 'blog/post_created.html')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog/post_list.html', {'posts': posts })


def post_detail(request, slug):
    posts = Post.objects.all().order_by('?')[:4]
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'post':post,'posts': posts })

