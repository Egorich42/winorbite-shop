#! /usr/bin/env python
# -*- coding: utf-8 -*-
from .models import *
from .forms import *
from cart.cart import Cart
from django.shortcuts import render
from django.core.mail import send_mail, send_mass_mail
from .values import *

def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            product = OrderItem.product  
            name = Order.email
            price = OrderItem.price
            order.save() 
            send_mail('Новый заказ','Пришел новый заказ'
                    +str(order.email)
                    +str(order.created),
                    from_who, clients)

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'orders/order/created.html', {'cart': cart,
                                                                 'order': order})

    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
