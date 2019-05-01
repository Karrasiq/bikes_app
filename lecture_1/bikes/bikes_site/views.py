from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
import json
from django.shortcuts import get_object_or_404
from django.utils import timezone


# Создайте представления, исходя из urls
def index(request):
    return HttpResponse('Hello, world. You\'re at the index.')

class CategoriesListView(ListView):
    model=Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MotobikeView(DetailView):
    model = Motobike

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
