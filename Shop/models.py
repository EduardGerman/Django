from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Category(models.Model):

	#Name category
	category_name = models.CharField(
		max_length = 60, blank = True, null = True, default = None)

	#Slug all category
	slug = models.SlugField(
		max_length = 200, db_index = True, unique = True)

	#Image for the main page
	category_img = models.ImageField(
		upload_to = 'media', null = True, blank = True)

	class Meta:
		ordering = ["category_name"]

		#
		verbose_name = "Категория"
		verbose_name_plural = "Категории"
			
	def  __str__(self):
		return self.category_name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args = [self.slug])
		
class Product(models.Model):

	#Inheriting from class "Category"
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	#Slug all products
	slug = models.SlugField(
		max_length = 200, db_index = True, default = None)
	
	#Product information

	product_name  = models.CharField(
		max_length = 60, blank = True, null = True, default = None)

	product_description  = models.TextField()

	product_img = models.ImageField(
		upload_to = 'media', null = True, blank = True)

	product_price = models.FloatField(default = 0.0)

	#
	available = models.BooleanField(default = True)

	product_stock = models.PositiveIntegerField(default = 0)


	class Meta:
		ordering = ["product_name"]
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"
		index_together = ["id", "slug"]

	def  __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args = [self.id, self.slug])
        


