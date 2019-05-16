from rest_framework import serializers

from .models import Product, Category


class CompanyProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'category_name')

    def get_category_name(self, obj):
        return obj.category.name if obj.category else ''


class CompanyProductCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category_name')

    def get_category_name(self, obj):
        return obj.category.name if obj.category else ''


class PublicProductSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'company_name')

    def get_company_name(self, obj):
        return obj.company.name if obj.company else ''


class PublicProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description')
