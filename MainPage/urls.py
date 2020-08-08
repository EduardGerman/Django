from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.content_list, name='content_list'),
]