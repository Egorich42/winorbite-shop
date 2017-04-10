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


<<<<<<< HEAD
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
=======
>>>>>>> 37507b5fd550b7e13e4051ab5f5864867e99b54e

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

<<<<<<< HEAD

=======
    return render(request, 'blog/post.html', {'post':post})
>>>>>>> 37507b5fd550b7e13e4051ab5f5864867e99b54e

