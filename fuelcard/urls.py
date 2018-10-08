# fuelcard/urls.py

from django.conf.urls import url
from fuelcard import views

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('report/', views.about, name='report'),
path('form/', vies.about, name='form'),
]
