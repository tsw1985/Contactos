# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from django.template import RequestContext

# Create your views here.

def home(request):
    # posts = Post.objects.all()
    contexto = {'posts' : ''}
    return render_to_response("home.html" , contexto)
