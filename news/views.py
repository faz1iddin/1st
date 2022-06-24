from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import News
from  django.urls import reverse_lazy
# Create your views here.

class HomePageView(ListView):
    model = News
    template_name = "home.html"

class HomeDetailView(DetailView):
    model = News
    template_name = "home_detail.html"

class HomeCreateView(CreateView):
    model = News
    template_name = 'new_post.html'
    fields = [
        "title", 'author', 'text',
    ]

class HomeUpdateView(UpdateView):
    model = News
    template_name = "renew_post.html"
    fields = ['title', 'text',]


class HomeDeleteView(DeleteView):
    model = News
    template_name = 'delete_post.html'
    success_url  = reverse_lazy('home')