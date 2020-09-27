from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'product_code', 'stock', 'price']
    search_fields = ['name', 'product_code']
    list_editable = ['stock', 'price']

    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)
