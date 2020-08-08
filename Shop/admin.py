from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'slug')
	prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'slug', 'product_price', 'product_stock', 'available']
	list_filter = ['available']
	list_editable = ['product_price', 'product_stock', 'available']
	prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)



