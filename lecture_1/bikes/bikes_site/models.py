from django.db import models


# Создайте модели, исходя из внешнего вида сайта
# Можно выделить категории, производителей и сами мототранспортные средства

class Category(models.Model):
    name = models.CharField(max_length=100)

    modified = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    modified = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)


class Motobike(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, models.CASCADE)
    category = models.ForeignKey(Category, models.CASCADE)
    description = models.TextField(default='', null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    image = models.ImageField(upload_to='bike_images', default='')

    modified = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
