from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from Cart.forms import CartAddProductForm


def product_list(request, category_slug = None):

	category = None

	categories = Category.objects.all()

	products = Product.objects.filter(available = True)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)

	cart_product_form = CartAddProductForm()

	data = {'category': category,'categories': categories,'products': products, 'cart_product_form': cart_product_form}

	return render(request, 'Shop/Shops.html', context = data)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id = id, slug = slug, available = True)

    categories = Category.objects.all()

    cart_product_form = CartAddProductForm()

    data = {'product': product, 'cart_product_form': cart_product_form,'categories': categories}

    return render(request, 'Shop/Product.html', context = data)