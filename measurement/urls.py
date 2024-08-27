from django.urls import path, include

from measurement.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sensor', SensorViewSet)
router.register(r'measurement', MeasurementViewSet)

urlpatterns = [
    path('v1/', include(router.urls))
]