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
            post.author = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})



def post_list(request):
    posts = Post.objects.all().order_by('id')

    return render(request, 'blog/post_list.html', {'posts': posts })



def post_detail(request, slug):
    posts = Post.objects.all().order_by('?')[:4]
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'post':post,'posts': posts })

