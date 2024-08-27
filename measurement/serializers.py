from rest_framework import serializers
from .models import Sensor, Measurement

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора, который принимает дополнительный аргумент fields,
    благодаря которому можно управлять отображением полей у моделей.
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