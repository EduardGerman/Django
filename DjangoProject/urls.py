from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include

from django.conf import settings
from django.views.static import serve

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
	#
	path('', include('MainPage.urls')),
	#
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    url(r'^Cart/', include('Cart.urls', namespace='cart')),

    url(r'^Orders/', include('Orders.urls', namespace='orders')),

    url(r'Catalog/', include('Shop.urls', namespace='shop')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

