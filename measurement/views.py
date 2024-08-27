from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action

class SensorViewSet(viewsets.ModelViewSet):
    """
    Представление для датчиков, в случае с детальной записью - выводится специальный
    сериализатор с измерениями.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SensorDetailSerializer
        else:
            return SensorSerializer
    
class MeasurementViewSet(viewsets.ModelViewSet):
    """
    Представление для измерений.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer