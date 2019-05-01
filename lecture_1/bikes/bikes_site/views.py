from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
# import json
# from django.shortcuts import get_object_or_404
# from django.utils import timezone


# Создайте представления, исходя из urls
def index(request):
    return HttpResponse('Hello, world. You\'re at the index.')


class CategoriesListView(ListView):
    queryset = Category.objects.all()


class CategoryView(DetailView):
    model = Category


class MotobikeView(DetailView):
    model = Motobike
