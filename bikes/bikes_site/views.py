from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Category, Product, Manager
from bikes_site.serializers import CompanyProductSerializer, PublicProductSerializer, PublicProductCategorySerializer


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


# LECTURE_2 VIEWS -->

class PublicProductPagination(PageNumberPagination):
    page_size = 5


class PublicProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PublicProductSerializer
    pagination_class = PublicProductPagination


class PublicProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PublicProductCategorySerializer
    pagination_class = PublicProductPagination

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, id=pk)
        products = self.get_queryset().filter(category=category)
        paginate = self.paginate_queryset(products)
        serializer = self.get_serializer(paginate, many=True)
        return self.get_paginated_response(serializer.data)


class CompanyProductViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyProductSerializer

    def get_queryset(self):
        manager = Manager.objects.get(user=self.request.user)
        return Product.objects.filter(company=manager.company)

    def perform_create(self, serializer):
        category_id = self.request.data.get('category')
        category = Category.objects.get(id=category_id)
        manager = Manager.objects.get(user=self.request.user)
        serializer.save(category=category, company=manager.company)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        updated_data = request.data
        for key, value in updated_data.items():
            setattr(instance, key, value)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CompanyProductCategoryViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        manager = get_object_or_404(Manager, user=self.request.user)
        category = get_object_or_404(Category, id=pk)
        products = Product.objects.filter(category=category, company=manager.company)
        serializer = CompanyProductSerializer(products, many=True)
        return Response(serializer.data)
# LECTURE_2 VIEWS <--
