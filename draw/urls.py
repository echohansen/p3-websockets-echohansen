# chat/urls.py
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('display/', views.display, name='display')
    
]

