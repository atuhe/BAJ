# fuelcard/urls.py


from django.conf.urls import url
from fuelcard import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.FormView.as_view()),
]
