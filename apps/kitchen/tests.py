from django.test import TestCase
from apps.kitchen.models import Ingredient

# Create your tests here.
ingredients = Ingredient.objects.all()
print(ingredients)