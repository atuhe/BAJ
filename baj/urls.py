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
from fuelcard.views import HomeView, PumpView, ReadingView, TankReadingsView, MeterReadingsView, SalesReport, Sales
from django.conf.urls.static import static

admin.site.site_header = "BAJ System admin"
admin.site.site_title = 'BAJ Service Stations Limited'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('readings/', ReadingView.as_view(), name='readings'),
    path('pumps/', PumpView.as_view(), name='pumps'),
    path('readings/tank/', TankReadingsView.as_view(), name='tank_readings'),
    path('readings/meter/', MeterReadingsView.as_view(), name='meter_readings'),
    path('sales/', SalesReport.as_view(), name='sales'),
    path('sales/other/', Sales.as_view(), name='other_sales'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
