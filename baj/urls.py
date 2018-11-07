"""baj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.conf import settings
from fuelcard.views import HomeView, PumpView, ReportView
from django.conf.urls.static import static

admin.site.site_header = "BAJ System admin"
admin.site.site_title = 'BAJ Service Stations Limited'


urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    # path('about/', TemplateView.as_view(template_name='report2.html'), name='forms-basic'),
    path('report/', ReportView.as_view(), name='report'),
    # path('form/', TemplateView.as_view(template_name='forms-advanced.html'), name='form')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
