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
                lambda itm: {
                    'name': itm.name,
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

    def serialize_category(self, moto_obj):
        return list(
            map(
                lambda itm: {
                    'name': itm.name,
                    'vendor': itm.company.name,
                    'category': itm.category.name,
                    'description': itm.description,
                },
                moto_obj
            )
        )

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        bikes_obj = Motobike.objects.filter(category=obj)
        data = self.serialize_category(bikes_obj)
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)


class MotobikeView(DetailView):
    model = Motobike
    template_name = 'motobike_detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')

        return {
            'name': obj.name,
            'vendor': obj.company.name,
            'category': obj.category.name,
            'description': obj.description,
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)
