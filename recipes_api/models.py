#Import - NOTE: To restrict our popularity field with min and max values, we import the validators from django.core.validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Recipes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True)
    main_ingredient = models.CharField(max_length=32)
    origin = models.CharField(max_length=32)
    #Here, we are using the validators parameter and defining a list of validators we want to add to the popularity field
    popularity = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )