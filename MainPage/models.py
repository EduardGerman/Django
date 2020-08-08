from django.db import models

class Slider(models.Model):
	slider_img = models.ImageField(
		upload_to='media', null=True, blank=True)
		