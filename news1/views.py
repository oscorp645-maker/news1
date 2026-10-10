from django.shortcuts import render
from news1.models import News1Model
from django.vievs.generic import ListView, DetailView
class News1ListView(ListView):
    model = NEWS1Model
    TEMPLATE_NAME = 'index.html'

# Create your views here.
