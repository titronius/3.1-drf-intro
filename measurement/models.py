from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length = 30, verbose_name = 'Название')
    description = models.TextField(default = '', blank = True, verbose_name = 'Описание')
    def __str__(self):
        return f"{str(self.id)} {self.name}"

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete = models.CASCADE, related_name='sensor', verbose_name = 'ID датчика')
    temp = models.DecimalField(max_digits = 3,decimal_places = 1, verbose_name = 'Температура')
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Дата и время измерения')
    image = models.ImageField(upload_to = 'measurement/images/',null = True, verbose_name = 'Изображение')
    
    def __str__(self):
        return f'{self.sensor} - {self.temperature}'