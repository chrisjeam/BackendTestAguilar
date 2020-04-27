from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return 'Sin {}'.format(self.name)

class Food(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type_f = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.name)

class Exeptions(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    def __str__(self):
        return 'Sin {}'.format(self.name)

class Combo(models.Model):    
    name = models.CharField(max_length=50)
    food = models.ManyToManyField(Food)
    def __str__(self):
        return '{}'.format(self.name)

class Menu(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    combo = models.ManyToManyField(Combo)
    