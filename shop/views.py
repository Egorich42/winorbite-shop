#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from blog.models import Post
from .values import *


def main(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('id')[:2]
    posts = Post.objects.all().order_by('id')[:1]
    
    return render_to_response('shop/product/main.html', {
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
    return render(request, 'shop/product/category.html', context_dict)



def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    product_category= product.category
    products = Product.objects.all().order_by('?')[:4]
    cart_product_form = CartAddProductForm()


    return render(request, 'shop/product/product_detail.html',
        {'product': product,'cart_product_form': cart_product_form,
         'product_category':product_category, 'products': products})


def categoryList(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('?')[:30]
    return render(request, 'shop/shop_main.html',{'categories':categories, 'products':products})

def paymentList(request):
    payment = payment_text[0] 
    return render(request, 'shop/singles/payment.html',{'payment':payment})

def contactList(request):
    contacts = contacts_text[0]
    return render(request, 'shop/singles/contact.html',{'contacts':contacts})


def privacy(request):
    privacy = privacy_text[0]
    return render(request, 'shop/singles/privacy.html',{'privacy':privacy})