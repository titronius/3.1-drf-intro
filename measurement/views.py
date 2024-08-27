from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        else:
            return SensorSerializer
    
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer