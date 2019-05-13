from django.contrib import admin
from .models import Category, Company, Product, Manager

# Register your models here.

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Manager)
