from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.formats.base_formats import XLSX 
from goods.models import Categories, Products


class ProductResource(resources.ModelResource):
    """Класс для управления импортом/экспортом товаров"""

    class Meta:
        model = Products
        fields = (
            'id',
            'name',
            'slug',
            'description',
            'price',
            'discount',
            'quantity',
            'category__name'
            )


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", ]


@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    resource_class = ProductResource 
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount", ]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
    ]

    formats = [XLSX]
