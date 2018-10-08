#fuelcard/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

	
	# Create your views here.
def index(request):
	return render(request, 'index.html', {})
		
def about(request):
	return render(request, 'forms-basic.html', {})

def report(request):
	return render(request, 'report.html', {})

def form(request):
	return render(request, 'forms-advanced.html', {})

