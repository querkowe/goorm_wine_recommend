
from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Wine_data(models.Model):

    country = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    designation = models.CharField(max_length=50)
    points = models.IntegerField(default =0) #(validators=[MinValueValidator(0), MaxValueValidator(5)])
    price = models.IntegerField(default =0)
    province = models.CharField(max_length=50)
    taster_name  = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    winery = models.CharField(max_length=50)
    year  = models.IntegerField(default =0)
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])

    class Meta:
        db_table = 'wine_data'