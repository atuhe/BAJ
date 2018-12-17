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
        fields = ['pump', 'opening_reading', 'closing_reading', 'transfers', 'net_sales']
        widgets = {
            'pump': Select(
                attrs={
                    'class': 'select2_demo_3 form-control',
                    'data-placeholder': 'Select Pump Name',
                    'tabindex': '1',
                    'id': 'pumpId'
                }
            ),
            'opening_reading': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'openingReadingId',
                    'required': 'required'
                }
            ),
            'closing_reading': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'closingReadingId',
                    'required': 'required'
                }
            ),
            'transfers': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'transfersId',
                    'required': 'required'
                }
            )
        }


class TankForm(ModelForm):
    class Meta:
        model = Tank
        fields = ['product_category', 'opening_stock', 'product_received', 'product_returned', 'closing_stock']
        widgets = {
            'product_category': Select(
                attrs={
                    'class': 'select2_demo_3 form-control',
                    'data-placeholder': 'Select Product',
                    'id': 'productId'
                }
            ),
            'opening_stock': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'openingStock',
                    'required': 'required'
                }
            ),
            'product_received': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'productReceived',
                    'required': 'required'
                }
            ),
            'product_returned': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'productReturned',
                    'required': 'required'
                }
            ),
            'closing_stock': NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'closingStock',
                    'required': 'required'
                }
            )
        }
