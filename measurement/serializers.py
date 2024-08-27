from rest_framework import serializers
from .models import Sensor, Measurement

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
 
class MeasurementSerializer(DynamicFieldsModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Measurement
        fields = "__all__"
        
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"
        
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(source = 'sensor', read_only = True, many = True, fields = ('temp', 'created_at'))
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']