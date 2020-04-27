from django.db import models
from datetime import datetime
from apps.kitchen.models import Combo

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Nombre')
    rut = models.CharField(max_length=30, unique=True, verbose_name='Rut')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Empleado'
        ordering = ['name']


class Order(models.Model):
    name = models.CharField(max_length=30, verbose_name='Nombre')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, verbose_name='Fecha')
    combos = models.ManyToManyField(Combo)