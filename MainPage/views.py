from django.shortcuts import render
from .models import Slider
from Shop.models import Category

def content_list(request):
	slider_list = Slider.objects.all()
	categories = Category.objects.all()
		
	data = {"slider_list" : slider_list, 'categories' : categories}

	return render(request, 'MainPage/Content.html', context=data)
