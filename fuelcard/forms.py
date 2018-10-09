from django.forms import (ModelForm, Select, TextInput, DateTimeInput, NumberInput)

from fuelcard.models import *


class PumpForm(ModelForm):
    class Meta:
        model = Pump
        fields = ['pump_name', 'pump_category', 'station_name']
        widgets = {
            'pump_name': Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Select Pump Name',
                    'tabindex': '1',
                    'style': 'text-transform: uppercase;'
                }
            ),
            'pump_category': Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Select Pump Category',
                    'tabindex': '1',
                    'style': 'text-transform: uppercase;'
                }
            ),
            'station_name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['date_created', 'pump', 'opening_reading', 'closing_reading', 'transfers', 'net_sales']
        widgets = {
            'date_created': DateTimeInput(
                attrs={

                }
            ),
            'pump': Select(
                attrs={
                    'class': 'standardSelect',
                    'data-placeholder': 'Select Pump Name',
                    'tabindex': '1',
                }
            ),
            'opening_reading': NumberInput(
                attrs={
                    'class': 'form-control mb-2 mr-sm-2'
                }
            ),
            'closing_reading': NumberInput(
                attrs={
                    'class': 'form-control mb-2 mr-sm-2'
                }
            ),
            'transfers': NumberInput(
                attrs={
                    'class': 'form-control mb-2 mr-sm-2'
                }
            )
        }
