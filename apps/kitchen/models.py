import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Sin {}'.format(self.name)
        
    class Meta:
        db_table = 'ingredient'
        ordering = ['name']

class Food(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type_f = models.CharField(max_length=50)
    exceptions = models.ManyToManyField(Ingredient, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'food'
        ordering = ['name']

class Combo(models.Model):    
    name = models.CharField(max_length=50)
    food = models.ManyToManyField(Food)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = 'combo'
        ordering = ['name']

class Menu(models.Model):
    date = models.DateField(unique=True)
    combo = models.ManyToManyField(Combo)
    uuid = models.UUIDField(null=True, default=uuid.uuid4, editable=False)

    class Meta:
        db_table = 'menu'
        ordering = ['id']
    
class Order(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, verbose_name='Fecha')
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    exceptions = models.ManyToManyField(Ingredient, blank=True)

    class Meta:
        db_table = 'order'
        ordering = ['id']   