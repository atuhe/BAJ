from rest_framework import serializers
from fuelcard.models import Report


class ReportSerializer(serializers.ModelSerializer):
    pump = serializers.SlugRelatedField(read_only=True, slug_field='pump_name')

    class Meta:
        model = Report
        fields = ('date_created', 'pump', 'opening_reading', 'closing_reading',
                  'meter_movement', 'transfers', 'net_sales')
