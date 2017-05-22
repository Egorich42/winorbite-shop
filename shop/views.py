#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from blog.models import Post

def ProductList(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('id')[:2]
    posts = Post.objects.all().order_by('id')[:1]
    
    return render_to_response('shop/product/list.html', {
        'categories': categories,'products': products, 'posts': posts,
        })


def category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        products = Product.objects.filter(category=category)
        cat_list = Category.objects.all()
        context_dict['products'] = products
        context_dict['category'] = category
        context_dict['cat_list'] = cat_list

    except Category.DoesNotExist:
        pass
    return render(request, 'shop/category.html', context_dict)



def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                             {'product': product,
                              'cart_product_form': cart_product_form})

def paymentList(request):
    return render(request, 'shop/payment.html')

def contactList(request):
    return render(request, 'shop/contact.html')

