from django.db import models
from Shop.models import Product

class Order(models.Model):
	
	#User name
	first_name = models.CharField(
		max_length=50, blank = True, null = True, default = None)
	last_name = models.CharField(
		max_length=50, blank = True, null = True, default = None)
	
	postal_code = models.CharField(
		max_length=20, blank = True, null = True, default = None)

	#User address
	city = models.CharField(
		max_length=100, blank = True, null = True, default = None)
	address = models.CharField(
		max_length=250, blank = True, null = True, default = None)

	email = models.EmailField()
	
	#
	created = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	paid = models.BooleanField(default = False)

	class Meta:
		ordering = ('-created',)

		#
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Order {}'.format(self.id)

	#The total value of the items purchased in this order.
	def get_total_cost(self):
		return sum(item.get_cost() 
			for item in 
				self.items.all())

class OrderItem(models.Model):

	#Inheriting from class "Order"
    order = models.ForeignKey(
    	Order, related_name = 'items', on_delete = models.CASCADE)

    #Inheriting from class "Product"
    product = models.ForeignKey(
    	Product, related_name = 'order_items', on_delete = models.CASCADE)


    price = models.DecimalField(
    	max_digits = 10, decimal_places = 2)

    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
