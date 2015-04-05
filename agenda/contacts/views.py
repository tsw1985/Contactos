# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic import DetailView, ListView , CreateView , UpdateView , DeleteView , FormView , View
from .models import Contact
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

#def home(request):
    # posts = Post.objects.all()
#    contexto = {'posts' : ''}
#    return render_to_response("home.html" , contexto)



class Home(TemplateView):
    def get(self, request , *args , **kwargs):
        return render_to_response('home.html')


class AddContact(CreateView):
    model = Contact
    success_url = reverse_lazy('home')
    # return render_to_response("home.html" , contexto)

class ListContact(ListView):
    model = Contact

