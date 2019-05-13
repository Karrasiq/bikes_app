from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
# import json
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Category, Product, Manager
from bikes_site.serializers import ProductSerializer


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

    def serialize_category(self, product_querylist):
        return list(
            map(
                lambda product_object: {
                    'name': product_object.name,
                    'vendor': product_object.company.name,
                    'category': product_object.category.name,
                    'description': product_object.description,
                },
                product_querylist
            )
        )

    def get_context_data(self, **kwargs):
        category_object = kwargs.get('object')
        product_object = Product.objects.filter(category=category_object)
        data = self.serialize_category(product_object)
        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)


class ProductView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        product_object = kwargs.get('object')

        return {
            'name': product_object.name,
            'vendor': product_object.company.name,
            'category': product_object.category.name,
            'description': product_object.description,
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context, safe=False)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        manager = Manager.objects.get(user=self.request.user)
        return Product.objects.filter(company=manager.company)


class CompanyProductCategoryViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        manager = get_object_or_404(Manager, user=self.request.user)
        category = get_object_or_404(Category, id=pk)
        products = Product.objects.filter(category=category, company=manager.company)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
