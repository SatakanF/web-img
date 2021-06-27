from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db import models
import import_export
from .models import Product, Logo
from import_export import resources
from import_export import fields
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
admin.site.register(Logo)




class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ['ukr_name', 'article', 'color_code']
    resource_class = ProductResource
    



admin.site.register(Product,ProductAdmin)
