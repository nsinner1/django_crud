from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DetailView
from .models import Books
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(ListView):
    template_name = 'home.html'
    model = Books


class DetailPageView(DetailView):
    template_name = 'detail.html'
    model = Books


class CreatePageView(CreateView):
    template_name = 'create.html'
    model = Books
    fields = '__all__'


class UpdatePageView(UpdateView):
    template_name = 'update.html'
    model = Books 
    fields = ['title', 'body']


class DeletePageView(DetailView):
    template_name = 'delete.html'
    model = Books
    success_url = reverse_lazy('home')