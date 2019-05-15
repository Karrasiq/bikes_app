from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# LECTURE_2 URLS -->
router = DefaultRouter()
router.register('products', views.PublicProductViewSet)
router.register('products/category', views.PublicProductCategoryViewSet, 'public_category')
router.register('company/products', views.CompanyProductViewSet, 'company_products')
router.register('company/products/category', views.CompanyProductCategoryViewSet, 'company_category')
# LECTURE_2 URLS <--

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoriesListView.as_view()),
    path('categories/<int:pk>/', views.CategoryView.as_view()),
    path('details/<int:pk>/', views.ProductView.as_view()),
    path('api/v1/', include(router.urls)),  # LECTURE_2 URLS
]
