from django.shortcuts import render
from news1.models import News1Model
from django.vievs.generic import ListView, DetailView, deleteView,
class News1ListView(ListView):
    model = NEWS1Model
    TEMPLATE_NAME = 'index.html'
class News1DetailView(DetailView):
    model = News1Model
    TEMPLATE_NAME = 'detail.html'
    class News1DeleteView(DeleteView):
        model = News1Model
        TEMPLATE_NAME = 'delete.html'
        success_url = '/'
# Create your views here.
