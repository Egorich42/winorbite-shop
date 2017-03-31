#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from .models import *
from django.http import HttpResponse
from .forms import *

def PostList(request):
    posts = Post.objects.all()
    return render(request, 'blog/postlist.html', {'posts': posts })


def PostDetail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'blog/post.html',
                             {'post': post})

