#fuelcard/views.py

from django.shortcuts import render
from django.views.generic import TemplateView

	
	# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'FUEL/index.html', context=None)
		
class FormView(TemplateView):
    def get (self, request, **kwargs):
        return render(request, 'FUEL/forms-basic.html', context=None)