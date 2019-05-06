from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from .models import Category, Motobike
# import json
# from django.shortcuts import get_object_or_404


# Создайте представления, исходя из urls
def index(request):
    return HttpResponse('Hello, world. You\'re at the index.')


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories_list.html'

    def serialize_categories_list(self, queryset):
        return list(
            map(
                lambda queryset_object: {
                    'name': queryset_object.name,
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        data = self.serialize_categories_list(context['object_list'])
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)


class CategoryView(DetailView):
    model = Category
    template_name = 'category_detail.html'

    def serialize_category(self, motobike_querylist):
        return list(
            map(
                lambda motobike_object: {
                    'name': motobike_object.name,
                    'vendor': motobike_object.company.name,
                    'category': motobike_object.category.name,
                    'description': motobike_object.description,
                },
                motobike_querylist
            )
        )

    def get_context_data(self, **kwargs):
        category_object = kwargs.get('object')
        motobike_object = Motobike.objects.filter(category=category_object)
        data = self.serialize_category(motobike_object)
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)


class MotobikeView(DetailView):
    model = Motobike
    template_name = 'motobike_detail.html'

    def get_context_data(self, **kwargs):
        motobike_object = kwargs.get('object')

        return {
            'name': motobike_object.name,
            'vendor': motobike_object.company.name,
            'category': motobike_object.category.name,
            'description': motobike_object.description,
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)
