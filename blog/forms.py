#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from .models import *


class write_post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'story',]

