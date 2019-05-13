from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('company/products', views.CompanyProductViewSet, 'company_products')
router.register('company/products/category', views.CompanyProductCategoryViewSet, 'category_detail')

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoriesListView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view()),
    path('details/<int:pk>/', views.ProductView.as_view()),
    path('api/v1/', include(router.urls)),
]
